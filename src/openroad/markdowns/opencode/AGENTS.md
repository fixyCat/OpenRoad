# OpenRoad — Agent Rules

## Core workflow

This repository uses:

- OpenRoad for roadmap sequencing
- OpenSpec for change proposal and execution

OpenRoad Items are the planning unit.
OpenSpec changes are the execution/spec unit.

By default, one OpenRoad Item should map to one OpenSpec change.

## Roadmap-first rule

When asked to make a feature, fix, refactor, or tooling change:

1. Read `openroad/roadmap.md` first, if it exists.
2. Select the next valid OpenRoad Item based on status, dependencies, and roadmap order.
3. Derive or reuse the corresponding OpenSpec change slug.
4. Run the OpenSpec proposal workflow for that Item before implementation.

Do not jump straight into coding when a roadmap exists.

## OpenRoad files

Check for and use:

- `openroad/roadmap.md`
- `openroad/status.md`
- `openroad/decisions.md`

If they do not exist, say so clearly.

## Roadmap context rule

When `openroad/roadmap.md` exists, read the roadmap context before selecting, proposing, implementing, or closing an Item.

This context includes:

- the introductory roadmap text above the Items list
- the current Phase text for the selected Item
- the current Milestone text for the selected Item

Treat this prose as required product context, not optional commentary. Use it to interpret item titles and summaries so domain terms are understood in context before generating or applying an OpenSpec change.

If an Item summary is ambiguous on its own, use the surrounding Phase and Milestone text to resolve that ambiguity before proceeding.

## OpenRoad Item requirements

Each roadmap Item must include:

- `id`
- `title`
- `status`
- `depends_on`
- `summary`
- `openspec_change`

If one or more fields are missing, report the issue before proceeding.

## Status meanings

Use these statuses consistently:

- `todo` — not yet proposed
- `proposed` — OpenSpec proposal exists and is ready for implementation
- `changed` — implementation and verification are complete and the OpenSpec change is ready for review and archive
- `done` — the OpenSpec change has been archived and the roadmap item is fully closed

Do not invent additional statuses unless the repository explicitly adopts them.

## Roadmap ordering rule

When selecting the next Item:

1. Read Items in top-to-bottom order as they appear in `openroad/roadmap.md`
2. Select the first Item whose:
   - `status` is `todo`
   - dependencies listed in `depends_on` are satisfied
3. Do not skip ahead to later Items if an earlier valid Item exists
4. Do not jump to a later milestone while valid Items remain in the current milestone unless explicitly instructed

If multiple Items appear valid, roadmap order decides.

## Dependency rule

Dependencies are satisfied only if all referenced Items have status `done`.

Items with blank `depends_on` are considered dependency-free.

If dependency references are missing or unclear, stop and explain the issue before proceeding.

## OpenSpec mapping rule

Each selected OpenRoad Item should map to exactly one active OpenSpec change by default.

Naming convention:

- Item ID remains stable in the roadmap
- OpenSpec change slug should be lowercase kebab-case
- OpenSpec change slug should begin with the lowercase Item ID

Example:

- Item: `GS-M1-001`
- title: `Create Initial Figma Plugin Shell`
- change slug: `gs-m1-001-create-initial-figma-plugin-shell`

If `openspec_change` is already set on the Item, reuse it.

Do not create multiple OpenSpec changes for the same Item unless explicitly required.

## Proposal-before-implementation rule

Before implementation:

1. Select the next valid Item
2. Read the surrounding Phase and Milestone context for that Item in `openroad/roadmap.md`
3. Run the OpenSpec propose flow for that Item
4. Ensure proposal artifacts are created
5. Only then proceed to implementation

Do not implement first and spec later.

## Explicit apply-gate rule

`/openroad` is proposal-only by default.

When running the OpenRoad workflow:

- select the next valid Item or explicit batch
- generate or reuse the OpenSpec proposal artifacts
- sync the roadmap to `proposed` where appropriate
- stop after proposal work is complete

Do not execute `/opsx-apply`, do not begin implementation, and do not modify implementation code for the selected Item unless the user explicitly requests implementation in the same instruction.

If the user says only `/openroad`, treat that as proposal-only.

## Existing proposal reuse rule

If the selected Item already has:

- `status: proposed`
- an `openspec_change` value
- and existing OpenSpec proposal artifacts for that change

then reuse that proposal rather than creating a new one.

Do not repropose an already proposed Item unless the user explicitly asks to refresh or regenerate the proposal artifacts.

## Changed and done item rules

If an Item has `status: changed`, do not repropose it. Treat it as implemented and awaiting review and archive.

If an Item has `status: done`, skip it.

Do not reopen or repropose `done` Items unless the user explicitly asks to revisit them.

## Batch mode rule

Default behavior is to process one Item at a time.

Batch mode is allowed only when the user explicitly requests multiple Items to be processed.

In batch mode:

1. Select Items in roadmap order
2. Only include Items whose dependencies are already satisfied
3. Use one OpenSpec change per OpenRoad Item
4. Do not merge multiple OpenRoad Items into a single OpenSpec change
5. Keep the batch small and controlled, usually 2 to 3 Items maximum unless explicitly instructed otherwise
6. Stop before including any Item whose dependencies are not yet satisfied

If batch selection becomes ambiguous, stop and explain the issue.

## Scope discipline

- Keep work scoped to the selected Item or explicit batch
- Do not bundle unrelated changes
- Do not silently fix nearby issues unless required
- Preserve existing workflows unless replacement is part of the selected Item

## Status sync rule

After OpenSpec proposal artifacts are created for an Item:

- set `openspec_change` if missing
- update Item `status` to `proposed`

After implementation and verification are complete:

- update Item `status` to `changed`

After the corresponding OpenSpec change is archived:

- update Item `status` to `done`

Do not mark `changed` or `done` early.

## Conflict handling

Stop and explain before proceeding if:

- roadmap dependencies are unclear
- roadmap fields are missing
- repo structure conflicts with roadmap assumptions
- existing OpenSpec change naming conflicts occur
- an Item is marked `proposed` but proposal artifacts cannot be found
- an Item is marked `changed` but the corresponding active or archived OpenSpec change cannot be found
- batch mode includes Items whose dependencies are not yet satisfied

In such cases, propose the smallest valid next step.
