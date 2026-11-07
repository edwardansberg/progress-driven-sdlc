"""One-off local Git fixture; leaves its temporary directory for inspection."""

import json
import os
from pathlib import Path
import subprocess
import tempfile


def main():
    root = Path(tempfile.mkdtemp(prefix="sdlc-staging-"))
    work = root / "work"
    origin = root / "origin.git"
    hooks = root / "empty-hooks"
    hooks.mkdir()
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(
        GIT_CONFIG_NOSYSTEM="1",
        GIT_CONFIG_GLOBAL=os.devnull,
        GIT_TERMINAL_PROMPT="0",
        GIT_AUTHOR_NAME="Codex",
        GIT_AUTHOR_EMAIL="codex@local.invalid",
        GIT_COMMITTER_NAME="Disposable fixture",
        GIT_COMMITTER_EMAIL="fixture@local.invalid",
        GIT_ALLOW_PROTOCOL="file",
    )

    def git(repo, *args):
        return subprocess.run(
            ["git", "-C", str(repo), *args],
            env=env,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout

    def refs(repo):
        return dict(
            line.split(" ", 1)
            for line in git(repo, "for-each-ref", "--format=%(refname) %(objectname)")
            .decode()
            .splitlines()
        )

    def unrelated_snapshot():
        return {
            "index_entry": git(work, "ls-files", "--stage", "--", "unrelated.txt"),
            "index_blob": git(work, "show", ":unrelated.txt"),
            "staged_diff": git(
                work, "diff", "--cached", "--binary", "--no-ext-diff",
                "--no-textconv", "--", "unrelated.txt"
            ),
            "working_bytes": (work / "unrelated.txt").read_bytes(),
        }

    def check(condition, message):
        if not condition:
            raise AssertionError(message)

    branch = "codex/staging-isolation"
    git(root, "init", "--bare", "--template=", "--initial-branch=main", str(origin))
    git(root, "init", "--template=", f"--initial-branch={branch}", str(work))
    for repo in (work, origin):
        git(repo, "config", "core.hooksPath", str(hooks))
    git(work, "config", "core.autocrlf", "false")
    git(work, "config", "core.filemode", "false")
    original = b"baseline unrelated content\n"
    owned = b"authorized owned change\n"
    (work / "owned.txt").write_bytes(b"baseline owned content\n")
    (work / "unrelated.txt").write_bytes(original)
    git(work, "add", "--", "owned.txt", "unrelated.txt")
    git(work, "commit", "-m", "Fixture baseline")
    git(work, "branch", "main")
    git(work, "tag", "fixture-base")
    git(work, "remote", "add", "origin", str(origin))
    git(work, "push", "origin", f"HEAD:refs/heads/{branch}", "main", "fixture-base")
    before_local = refs(work)
    before_remote = refs(origin)
    baseline = git(work, "rev-parse", "HEAD").decode().strip()

    staged = original + b"pre-existing staged edit\n"
    (work / "unrelated.txt").write_bytes(staged)
    git(work, "add", "--", "unrelated.txt")
    git(work, "update-index", "--chmod=+x", "--", "unrelated.txt")
    (work / "unrelated.txt").write_bytes(staged + b"additional unstaged edit\r\n")
    before_unrelated = unrelated_snapshot()
    check(before_unrelated["index_entry"].startswith(b"100755 "), "Fixture mode missing")
    check(before_unrelated["staged_diff"], "Fixture staged difference missing")
    check(git(work, "diff", "--", "unrelated.txt"), "Fixture unstaged difference missing")
    (work / "owned.txt").write_bytes(owned)

    # Stage one inspected path; --only commits its authorized working contents.
    git(work, "add", "--", "owned.txt")
    check(git(work, "show", ":owned.txt") == owned, "Unexpected owned staged contents")
    check(not git(work, "diff", "--", "owned.txt"), "Owned unstaged changes exist")
    check(
        set(git(work, "diff", "--cached", "--name-only").decode().splitlines())
        == {"owned.txt", "unrelated.txt"},
        "Unexpected staged paths",
    )
    check(unrelated_snapshot() == before_unrelated, "Staging altered unrelated work")
    git(work, "diff", "--cached", "--check")
    git(work, "commit", "--only", "-m", "Commit authorized owned change", "--", "owned.txt")
    candidate = git(work, "rev-parse", "HEAD").decode().strip()
    check(unrelated_snapshot() == before_unrelated, "Commit altered unrelated work")
    check(git(work, "rev-parse", "HEAD^").decode().strip() == baseline, "Unexpected parent")
    check(
        git(work, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD")
        == b"owned.txt\n",
        "Commit contains unexpected changed paths",
    )
    check(git(work, "show", "HEAD:owned.txt") == owned, "Owned tree content differs")
    check(git(work, "show", "HEAD:unrelated.txt") == original, "Unrelated edits committed")
    check(
        git(work, "ls-tree", "HEAD", "--", "unrelated.txt")
        == git(work, "ls-tree", baseline, "--", "unrelated.txt"),
        "Unrelated committed blob or mode changed",
    )
    expected_local = dict(before_local, **{f"refs/heads/{branch}": candidate})
    check(refs(work) == expected_local, "Commit changed another local ref")
    check(refs(origin) == before_remote, "Commit changed a remote ref")
    metadata = git(work, "show", "-s", "--format=fuller", "HEAD")
    check(b"Codex <codex@local.invalid>" in metadata, "Unexpected fixture author")
    check(b"Disposable fixture <fixture@local.invalid>" in metadata, "Unexpected fixture committer")
    git(work, "push", "origin", f"HEAD:refs/heads/{branch}")
    check(
        git(work, "ls-remote", "--heads", "origin", f"refs/heads/{branch}")
        == f"{candidate}\trefs/heads/{branch}\n".encode(),
        "Remote candidate differs",
    )
    expected_local[f"refs/remotes/origin/{branch}"] = candidate
    expected_remote = dict(before_remote, **{f"refs/heads/{branch}": candidate})
    check(refs(work) == expected_local, "Push changed another local ref")
    check(refs(origin) == expected_remote, "Push changed another remote ref")
    check(unrelated_snapshot() == before_unrelated, "Push altered unrelated work")
    check(git(work, "symbolic-ref", "HEAD") == f"refs/heads/{branch}\n".encode(), "Branch changed")
    print(json.dumps({
        "result": "Passed",
        "fixture": str(root),
        "candidate": candidate,
        "method": "Explicit path staging; git commit --only; ordinary local push; exact ls-remote",
        "preserved": "Unrelated index blob/mode/staged diff and working bytes; all other refs",
        "limits": "Disposable local Git only; owned path fully authorized; no real hooks/CI/hosting",
    }, indent=2))


if __name__ == "__main__":
    main()
