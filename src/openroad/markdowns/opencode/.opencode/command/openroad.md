---
description: Select the next OpenRoad item or small batch and run the OpenSpec propose flow
---

You are running the OpenRoad workflow for this repository.

Your purpose is to bridge:

- OpenRoad Item selection and ordering
- OpenSpec change proposal generation

## Step 1 — Read project instructions and roadmap

Read these files first:

- @AGENTS.md
- @openroad/roadmap.md

Also read if present:

- @openroad/status.md
- @openroad/decisions.md

Do not begin implementation yet.

Before selecting an Item, also read the roadmap prose context around the candidate work:

- the introductory text above `## Items`
- the current Phase text
- the current Milestone text

Use that context to interpret item titles and summaries before deriving the OpenSpec change.

## Step 2 — Select the next valid OpenRoad Item or batch

By default, select only one Item.

Only select multiple Items if the user explicitly requests batch mode.

When selecting Items from `openroad/roadmap.md`:

1. Identify all roadmap Items in top-to-bottom order
2. Find the first Item whose:
   - `status` is `todo`
   - dependencies in `depends_on` are satisfied
3. Select only that one Item by default
4. Identify the Phase and Milestone section that contain the selected Item so their text can be used as proposal context

In batch mode:

1. Continue scanning downward in roadmap order
2. Add only Items whose:
   - `status` is `todo`
   - dependencies are already satisfied
3. Stop when:
   - the requested batch size is reached
   - an Item has unsatisfied dependencies
   - selection becomes ambiguous

Do not skip earlier valid Items in favor of later ones.

If no valid Item exists, stop and explain why.

If the roadmap is missing required fields or is ambiguous, stop and explain the issue.

## Step 3 — Handle existing proposals

For each selected Item:

1. Read `id`, `title`, `summary`, and `openspec_change`
2. If the Item has `status: done`, skip it
3. If the Item has `status: changed`, report that it is awaiting close/archive and skip it
4. If the Item has `status: proposed` and the existing OpenSpec proposal artifacts already exist:
   - reuse the existing proposal
   - do not create a new one
5. If the Item has `status: proposed` but proposal artifacts cannot be found:
   - stop and explain the inconsistency
6. If the Item has `status: todo`, continue to Step 4

Do not repropose an already proposed Item unless the user explicitly asks to refresh or regenerate the proposal.

## Step 4 — Derive the OpenSpec change identity

For each selected `todo` Item, extract:

- Item ID
- title
- summary

Generate an OpenSpec change slug using:

- lowercase
- kebab-case
- prefixed with the lowercase Item ID

Example:

- Item ID: `GS-M1-001`
- title: `Create Initial Figma Plugin Shell`
- slug: `gs-m1-001-create-initial-figma-plugin-shell`

If the Item already has an `openspec_change` value, use that instead of generating a new one.

## Step 5 — Produce a brief before proposing

Before continuing, output a short execution brief.

For single-item mode, include:

- selected Item ID
- selected Item title
- current Phase
- current Milestone
- dependency status
- chosen OpenSpec change slug
- Item summary
- relevant roadmap context from the Phase and Milestone text
- expected OpenSpec artifact location

For batch mode, include the same details for each selected Item in roadmap order.

Do not implement code yet.

## Step 6 — Run the OpenSpec propose flow

For each selected Item with `status: todo`, perform the equivalent of the `/opsx-propose` workflow.

Use:

- the OpenSpec change slug as the change name
- the Item summary as the natural-language change description

Your goal is to create or update the OpenSpec change and generate the required proposal artifacts until the change is ready for the next OpenSpec stage.

Follow the same artifact-generation discipline used by `opsx-propose`.

Do not skip required artifacts.

This workflow is proposal-only by default.
Stop after proposal artifacts are created or reused.

Do not execute `/opsx-apply`.
Do not begin implementation.
Do not modify implementation code for the selected Item unless the user explicitly requested implementation in the same instruction.

If an Item was already `proposed` and valid proposal artifacts exist, report that it was reused and do not repropose it.

## Step 7 — Sync the roadmap

After OpenSpec proposal artifacts are generated for each newly proposed Item:

1. Report the resulting OpenSpec change slug
2. Report the files created or updated
3. Update the selected Item in `openroad/roadmap.md` so that:
   - `openspec_change` is set to the chosen slug if not already set
   - `status` becomes `proposed`

For reused Items that were already `proposed`, do not change status unless another explicit roadmap update is required.

Do not mark any Item as `changed` or `done` in this workflow.

## Step 8 — Final output

At the end, report:

- whether OpenRoad ran successfully
- selected OpenRoad Item or batch
- OpenSpec change slug or slugs
- generated or reused proposal artifacts
- whether each change is ready for `/opsx-apply`
- the next likely OpenRoad Item after this run
