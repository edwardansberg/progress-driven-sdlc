# Checkpoint Briefing Examples

These fictional snapshots illustrate the [canonical checkpoint briefing](../README.md#checkpoint-briefing). Read when a concrete example helps; they are not live project state, permission or a second briefing template. Each source reference below describes an imaginary record and revision, not an existing file or verified result. In a real briefing, use an accessible source reference.

Adapt the labels and tone to the person and decision. Milestones describe useful outcomes. The core owns presentation and save-and-reuse rules; these examples illustrate the visible briefing text.

## Planning: choose a business rule

This checkpoint: The existing booking flow is mapped. One business rule remains open: allow moves until the class starts, or stop them two hours earlier. The earlier cutoff gives staff preparation time but gives customers less flexibility. No product change has been implemented.

Current goal: Let customers move a class booking without calling reception.

Status: Planning. Source: Fictional `feat-move-booking`, detailed record revision `plan-2`; inspected application snapshot `booking-base-1`.

Needs attention: The agent cannot infer the cancellation policy from the current screen. A documented rule is needed before implementing the cutoff.

Your next move: Business owner chooses the cutoff. The agent will continue the independent navigation investigation while that decision is pending.

## Implementation: a useful milestone

This checkpoint: The first working route now carries a saved pickup from the list into its packing screen. Local checks passed for saving, reopening and retaining item quantities. Staff can try that route in the review build; label printing is still being connected.

Current goal: Help warehouse staff prepare a pickup without re-entering item details.

Status: Implementing. Source: Fictional `feat-pickup-packing`, detailed record revision `build-3`; review build `pickup-candidate-2`.

Needs attention: The checks used sample orders. They do not establish that the warehouse printer works or that staff find the screen easy to use.

Your next move: Nothing is needed from you now. The agent will finish the authorized printing connection and run its agreed checks before requesting review.

## Failed verification: explain the consequence

This checkpoint: Verification failed: a name containing a comma became two columns in the exported file. The export is not ready for your review. The check found a defect before publication; it did not change the original member records.

Current goal: Export a monthly membership list without losing names.

Status: Implementing. Source: Fictional `fix-member-export`, detailed record revision `check-4`; local candidate `export-candidate-1`.

Needs attention: The required quoted-field check is Failed. A successful export of simple names does not cover this case.

Your next move: Nothing is needed from you now. The agent will repair the field quoting and rerun the affected checks within the approved scope.

## Human validation: ready to try

This checkpoint: In the tested review environment, repeated clicks reused the same report job. The duplicate-request and error-recovery checks passed for the identified build. The source candidate is published; production is unchanged.

Current goal: Prevent a repeated click from starting the same report twice.

Status: Ready for user validation. Source: Fictional `fix-report-repeat`, detailed record revision `review-5`; published source and review build `report-candidate-3`.

Needs attention: Human acceptance is Pending. Automated checks do not establish that the waiting message is clear to your team. Deployment needs its separate release decision.

Your next move: Business owner tries repeated clicks and the waiting message in the review environment, then accepts this candidate or describes the needed correction.

## Accepted development: delivery still pending

This checkpoint: You accepted the corrected hours and mobile layout in review build `hours-candidate-2`. Development is Completed and archived. Production still shows the previous hours because deployment is pending; this checkpoint does not claim release.

Current goal: Make corrected opening hours available to customers.

Status: No active workstream. Source: Fictional `fix-opening-hours`, archived detailed record revision `accepted-6`, accepted artifact `hours-candidate-2`; pending delivery record `release-hours-7`.

Needs attention: The delivery owner has the agreed handoff. Production content and mobile-layout checks remain Pending in that delivery record and still govern release acceptance.

Your next move: Nothing is needed from you now. The assigned release owner will deploy the accepted artifact under the recorded release authority, run those checks and update the delivery record. The archive keeps its original closeout observation.
