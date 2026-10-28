# How the depth interval fills itself in

How a borehole's `top`, `bottom` and `vertical_depth` stay consistent, and why. It does not cover the
field definitions, which the [model reference](../reference/models.md) lists.

## Three values, two of which are enough

A depth interval can be described by where it starts and ends, or by where it starts and how long it
is. Data arrives in either form, so the model accepts any two of the three values and works out the
third when the record is saved:

- With `top` and `bottom`, it sets `vertical_depth` to the distance between them.
- With `top` and `vertical_depth`, it sets `bottom` to `top` plus the depth.
- With `bottom` and `vertical_depth`, it sets `top` to `bottom` minus the depth.
- With only `vertical_depth`, it sets `top` to zero and `bottom` to the depth.

When all three are given, `vertical_depth` is recalculated from `top` and `bottom`, so the three
cannot disagree after a save.

## Depth is positive downward

For a geological depth interval, `top` and `bottom` are measured downward from the vertical datum, so
`bottom` is greater than `top`. A database constraint enforces this on boreholes, and a record that
breaks it is rejected on save, whichever way it was written.

The constraint sits in the database and not only in the model so that a bulk import or a direct
query cannot store an interval the model would refuse.

## Why the field is not called depth

The depth field is named `vertical_depth` because `depth` would clash with the `depth` field that django-treebeard adds to
the sample model's tree structure.
