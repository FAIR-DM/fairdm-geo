# fairdm-geo — Context

The words this repository uses, what each one means here, and the words it avoids. Issues, pull
requests, code and tests use these terms. FairDM's own terms (portal, dataset, sample) mean what
they mean in FairDM.

## Glossary

**Portal**
A FairDM site that installs this package. _Avoid_: project, app, instance.

**Sample**
A physical thing collected or prepared for study: a rock sample, a drill core, a thin section, and
also the place it came from, since FairDM records sampling locations as samples too. Every model
here builds on FairDM's `Sample`. _Avoid_: specimen (ODM2's word, kept only in the names of ODM2
vocabularies such as "specimen type").

**Earth sample**
A sample from the solid Earth. `GenericEarthSample` is the abstract base for every sample model in
the package. _Avoid_: geo sample, geological sample.

**Rock sample**
A sample of rock: the general `RockSample`, or one of its prepared forms, a drill core, drill
cuttings, a thin section or rock powder. _Avoid_: specimen, hand sample (unless that is meant).

**Sampling location**
The place a sample was taken from, recorded as a sample in its own right with a location.
_Avoid_: site (ODM2's word, used only in "site type"), station, locality.

**Borehole**
A sampling location that is a drilled hole, with a geometry (azimuth, inclination, length) and a
depth interval. _Avoid_: well, drill hole.

**Hole**
The geometry a borehole carries: azimuth, inclination and length. `GenericHole` holds it.

**Depth interval**
The stretch of a hole between a top and a bottom, measured downward from the vertical datum, with
the lithology, geologic time and stratigraphic units found there. A borehole has one. The bottom
is never above the top. _Avoid_: section, run, segment.

**Vertical datum**
The reference point a depth interval is measured from. _Avoid_: datum on its own.

**Lithology**
The rock type of a depth interval, as concepts from the CGI Simple Lithology vocabulary.
_Avoid_: rock type (except in prose), petrology.

**Stratigraphic unit**
A named body of rock with a rank (formation, member, group and so on) and a genesis, both from CGI
vocabularies. _Avoid_: layer, stratum.

**Geologic time**
The age of a depth interval, as concepts from the International Chronostratigraphic Chart.
_Avoid_: era (one rank of it), period.

**Vocabulary**
A published controlled vocabulary (a SKOS concept scheme), shipped with the package as a file and
loaded into the portal by django-controlled-vocabularies. _Avoid_: choices, enumeration, list.

**Concept**
One term in a vocabulary, identified by its URI. A model field holds a concept. _Avoid_: term,
choice, keyword.
