"""One-off local Markdown path/fragment check for this workstream; no network."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
files = [root / 'AGENTS.md', root / 'README.md', *sorted((root / 'docs').rglob('*.md'))]
errors = []
checked = 0


def prose(path):
    text = path.read_text(encoding='utf-8-sig')
    return re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text,
                  flags=re.M | re.S)


def anchors(path):
    text = prose(path)
    found = set(re.findall(r'<a\s+id=[\"\']([^\"\']+)', text))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        suffix = counts.get(slug, 0)
        counts[slug] = suffix + 1
        found.add(f'{slug}-{suffix}' if suffix else slug)
    return found


for source in files:
    text = prose(source)
    refs = dict(re.findall(r'^\[([^\]]+)\]:\s*(\S+)', text, re.M))
    targets = re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', text)
    for label in re.findall(r'!?\[[^\]\n]+\]\[([^\]\n]+)\]', text):
        if label not in refs:
            errors.append(f'{source.relative_to(root)}: missing reference {label}')
        else:
            targets.append(refs[label])
    for target in targets:
        target = target.split(' "', 1)[0].strip('<>')
        url = urlsplit(target)
        if url.scheme or url.netloc:
            continue
        dest = (source.parent / unquote(url.path)).resolve() if url.path else source
        checked += 1
        if not dest.is_relative_to(root) or not dest.exists():
            errors.append(f'{source.relative_to(root)}: missing/escaping {target}')
        elif url.fragment and dest.suffix == '.md' and unquote(url.fragment) not in anchors(dest):
            errors.append(f'{source.relative_to(root)}: missing anchor {target}')
print(f'{len(files)} Markdown files; {checked} local links/fragments; {len(errors)} errors')
for error in errors:
    print(error)
sys.exit(bool(errors))
