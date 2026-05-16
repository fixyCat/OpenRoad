---
description: Close changed OpenRoad items by archiving their OpenSpec changes and marking roadmap items as done
---

You are running the OpenRoad close workflow for this repository.

Your purpose is to bridge:

- completed OpenSpec changes
- OpenRoad roadmap completion
- archive and status synchronization

## Step 1 — Read project instructions and roadmap

Read these files first:

- @AGENTS.md
- @openroad/roadmap.md

Also read if present:

- @openroad/status.md
- @openroad/decisions.md

Do not begin implementation work.

## Step 2 — Identify the item or batch to close

By default, close only one Item.

Only close multiple Items if the user explicitly requests batch mode.

When selecting Items from `openroad/roadmap.md`:

1. Identify roadmap Items in top-to-bottom order
2. Select Items whose:
   - `status` is `changed`
   - `openspec_change` is set
3. In default mode, select only the first matching Item unless the user specifies a particular Item ID
4. In batch mode, continue in roadmap order until the requested batch size is reached

If the user specifies one or more Item IDs, use those Items instead of auto-selection.

If no valid Item exists, stop and explain why.

## Step 3 — Validate close readiness

For each selected Item, extract:

- `id`
- `title`
- `status`
- `summary`
- `openspec_change`

Then verify:

1. the Item is currently `changed`
2. the corresponding OpenSpec change exists
3. the change appears completed and ready for archive according to the repository's OpenSpec workflow

If an Item is already `done`, report it and skip it.

If an Item is `todo`, stop and explain that it has not yet been proposed.

If an Item is `proposed`, stop and explain that implementation is not yet marked complete in the roadmap.

If a change cannot be found, stop and explain the inconsistency.

If the change exists but does not appear ready for archive, stop and explain what still appears open.

Do not mark any Item `done` unless the associated OpenSpec change is ready to archive and the roadmap item is currently `changed`.

## Step 4 — Produce a brief before closing

Before continuing, output a short execution brief.

For single-item mode, include:

- selected Item ID
- selected Item title
- current roadmap status
- OpenSpec change slug
- archive readiness status
- expected archive action

For batch mode, include the same details for each selected Item in roadmap order.

## Step 5 — Run the OpenSpec archive flow

For each validated Item, perform the equivalent of the OpenSpec archive/close workflow for the associated `openspec_change`.

Your goal is to archive the completed change using the repository's normal OpenSpec archive discipline.

Do not skip required archive artifacts or status transitions.

If the change is already archived, report that and continue without error.

## Step 6 — Sync the roadmap

After the OpenSpec archive flow succeeds for each Item:

1. report the archived OpenSpec change slug
2. report the files created or updated
3. update the selected Item in `openroad/roadmap.md` so that:
   - `status` becomes `done`

Keep the existing `openspec_change` value intact.

Do not clear the change slug unless the repository explicitly requires that behavior.

## Step 7 — Final output

At the end, report:

- whether OpenRoad close ran successfully
- the closed OpenRoad Item or batch
- the archived OpenSpec change slug or slugs
- the files created or updated
- whether roadmap sync was completed
- the next likely OpenRoad Item ready for `/openroad`