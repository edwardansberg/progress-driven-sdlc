# Application Experience

Read for a new interactive application's first working slice, an explicitly scoped UI redesign, or changes to the interactions below. This is application guidance, not required reading for unrelated coding work. [Core policy](../README.md) owns authority and development gates.

## First working slice

Establish a usable interaction shell around one real workflow connected end to end. Include application/workspace identity, current location, consistent main navigation, relevant actions and help, truthful operational status, and recoverable error feedback. Validate that structure early; add subsequent features within it. A decorative dashboard with disconnected controls does not satisfy this milestone.

Before changing an existing product, inspect its navigation, users and local constraints. Framework adoption alone does not authorize a UI migration. For an API, library or command-line tool, define appropriate commands, results and observability without inventing a frontend. The optional [Project Blueprint](project-blueprint.md) explains the project; it is separate from the application's controls and any execution controller.

## Predictable access and context

“Always accessible” means users can predictably reach relevant controls and status. Make frequent actions directly reachable; put secondary actions in clearly labelled menus or panels. At narrow widths and zoom, controls may move or collapse. Preserve useful scrolling, readable content and modal focus behavior; fixed panels must not obscure content or focused controls.

Preserve relevant inputs, selection and task context across navigation where appropriate. Define what persists, for how long, and what happens before navigation could lose unsaved work. Show existing capabilities; label prototype or unavailable controls clearly and explain their limits.

Derive operational status from actual system evidence. Distinguish running, completed, failed, unavailable and stale observations, plus cancellation requested versus confirmed where applicable. Show freshness when it affects interpretation. Never invent percentages, successful cancellation, monitoring, rollback or undo. Give useful recovery steps and explain unavailable actions in ordinary language; keep technical detail available on demand.

Runtime status, development progress and permission are separate. A visible button grants no authority. Pointer, touch, keyboard and shortcut actions must share authorization and validation, including server-side enforcement where relevant.

## Keyboard, pointer and focus

Use current WCAG and ARIA Authoring Practices guidance for web interaction, and equivalent platform conventions for native applications.

- Use semantic controls, useful labels, logical focus order and visible unobscured focus. `Tab` and `Shift+Tab` move between controls/components; arrows operate within widgets that use that pattern. Preserve ordinary scrolling and text editing. See [APG keyboard interaction](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/).
- Preserve native activation: [buttons](https://www.w3.org/WAI/ARIA/apg/patterns/button/) use `Enter` or `Space`; [links](https://www.w3.org/WAI/ARIA/apg/patterns/link/) use `Enter`. Do not impose one key behavior on every element. Important actions need both a visible pointer/touch path and a complete standard keyboard path.
- Move focus deliberately after dynamic changes. In a modal, move focus inside, make the background inert and contain its tab sequence. Provide a visible close action. `Escape` dismisses the active dismissible layer; restore focus to its invoker or a logical successor. Dismissal must not silently reset data or cancel a background job. Avoid traps outside the intended modal interaction. See [APG modal dialogs](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).
- WASD is optional, off by default, scoped and discoverable. Allow disabling it or remapping it to include a non-character key. Never activate it during text entry, editable content or input composition. Avoid operating-system, browser and assistive-technology conflicts. These defaults are this framework's design choice; [WCAG character shortcuts](https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html) allows turn-off, remapping or activation only while the relevant component has focus.
- Use text or other cues alongside color, sufficient contrast, responsive reflow and reduced motion where motion exists. Follow the applicable [WCAG 2.2 criteria](https://www.w3.org/TR/WCAG22/). Announce relevant [status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) programmatically without repeatedly moving focus or interrupting work.

## Application acceptance evidence

Define checks for the actual main workflow and record the candidate, environment, results and limitations in the existing workstream. Include:

- Complete the workflow using standard keyboard controls alone, then pointer/touch separately; check equivalent authorization, validation and unavailable-action feedback.
- Navigate away and back with relevant inputs and unsaved work; verify the agreed persistence and loss-prevention behavior.
- Exercise text editing and input composition, with optional shortcuts disabled and enabled; check that typing cannot activate navigation or actions.
- Open and close modal layers; inspect initial focus, contained traversal, background interaction, dismissal and restored focus. Check focus after errors and other dynamic updates.
- Test vertical content at 320 CSS-pixel width and at 400% zoom from a 1280 CSS-pixel-wide viewport. Preserve information and functionality without two-dimensional scrolling. Apply exceptions only to regions whose meaning or use needs two dimensions, such as a map or data table; surrounding controls and individual table cells still reflow. For horizontal content, check the equivalent 256 CSS-pixel height. See [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
- Check labels, contrast, non-color cues, reduced motion and relevant announcements with the supported assistive technology. Exercise actual failure, unavailable/stale status and cancellation transitions where implemented.

Automated accessibility checks cover only some defects. They do not establish complete accessibility, human usability, correct focus behavior or reliable operation across supported devices and assistive technologies. Documentation walkthroughs establish none of those runtime outcomes.

Reference basis: W3C pages above checked 2026-11-07; WCAG 2.2 Recommendation dated 2024-12-12. Understanding pages and APG are informative guidance, not extra normative conformance criteria. The first-slice structure, persistent context and shortcut defaults are design choices to validate in the application, not measured benefits of this documentation.
