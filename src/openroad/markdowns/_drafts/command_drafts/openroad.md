---
description: Select the next OpenRoad item and run the OpenSpec propose flow for it
---

You are running the OpenRoad workflow for this repository.

Your purpose is to bridge:

- OpenRoad Item selection and ordering
- OpenSpec change proposal generation

## Step 1 — Read project instructions and roadmap

Read these files first:

- @AGENTS.md
- @OpenRoad/roadmap.md

Also read if present:

- @OpenRoad/status.md
- @OpenRoad/decisions.md

Do not begin implementation yet.

## Step 2 — Select the next valid OpenRoad Item

From `openroad/roadmap.md`:

1. Identify all Items.
2. Find the next Item whose:
   - `status` is `todo`
   - dependencies in `depends_on` are satisfied
3. Select only one Item.

If no valid Item exists, stop and explain why.

If the roadmap is missing required fields or is ambiguous, stop and explain the issue.

## Step 3 — Derive the OpenSpec change identity

From the selected Item, extract:

- Item ID
- title
- summary

Generate an OpenSpec change slug using:

- lowercase
- kebab-case
- prefixed with the Item ID

Example:

- Item ID: `OR-ML-002`
- title: `Implement automated review detectors`
- slug: `or-ml-002-implement-automated-review-detectors`

If the Item already has an `openspec_change` value, use that instead of generating a new one.

## Step 4 — Produce a brief before proposing

Before continuing, output a short execution brief containing:

- selected Item ID
- selected Item title
- dependency status
- chosen OpenSpec change slug
- Item summary
- expected OpenSpec artifact location

Do not implement code yet.

## Step 5 — Run the OpenSpec propose flow

Now perform the equivalent of the `/opsx-propose` workflow for the selected Item.

Use:

- the OpenSpec change slug as the change name
- the Item summary as the natural-language change description

Your goal is to create or update the OpenSpec change and generate the required proposal artifacts until the change is ready for the next OpenSpec stage.

Follow the same artifact-generation discipline used by `opsx-propose`.

Do not skip required artifacts.

Do not begin implementation unless explicitly instructed by the OpenSpec workflow or the user.

## Step 6 — Sync the roadmap

After the OpenSpec proposal artifacts are generated:

1. Report the resulting OpenSpec change slug
2. Report the files created or updated
3. Update the selected Item in `openroad/roadmap.md` so that:
   - `openspec_change` is set to the chosen slug if not already set
   - `status` becomes `proposed`

Do not mark the Item as `done` unless implementation and verification are complete.

## Step 7 — Final output

At the end, report:

- if OpenRoad ran successfully
- selected OpenRoad Item
- OpenSpec change slug
- generated proposal artifacts
- whether the change is ready for `/opsx-apply`
- the next likely OpenRoad Item after this one
