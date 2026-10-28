# Domain Docs

How an agent should read this repo's domain documentation before working on the codebase.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root: the vocabulary this repository uses, and the words it
  deliberately avoids.
- **`docs/adr/`**, when it exists: the decisions that touch the area you are about to work in.

If any of these files don't exist, proceed silently. Don't flag their absence, and don't suggest
creating them upfront.

## File structure

Single-context repo:

```
/
├── CONTEXT.md
├── CONSTITUTION.md
├── docs/adr/        (created when the first decision is recorded)
└── fairdm_geo/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, say, or a test name), use the term as
defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids. Two are worth
repeating:

- The physical thing is a **sample**, never a specimen. "Specimen" appears only in the names of
  ODM2 vocabularies.
- Terms come from a published **vocabulary** and a field holds a **concept**. Never add
  `choices` or `TextChoices` for a term a published vocabulary covers.

## Flag conflicts with a recorded decision

If your output contradicts a decision in `docs/adr/`, surface it explicitly rather than silently
overriding it.
