# Models

The models `fairdm-geo` provides, by the app that holds them. Every concrete model is a FairDM
`Sample`, so it also has the fields FairDM gives every sample, such as `name`, `local_id`,
`dataset`, `status` and `location`. Those fields are described in FairDM's documentation and are
not repeated here.

Fields that take a term name the vocabulary they draw from. The [vocabularies
page](vocabularies.md) describes each one.

## Sampling locations

The `fairdm_geo.sites` app (label `fairdm_geo_sites`).

### SamplingLocation

A specific place where samples are collected.

| Field | Type | Default | Description |
|---|---|---|---|
| `type` | Concept | `http://vocabulary.odm2.org/sitetype/unknown` | The type of sampling location. Vocabulary: ODM2 Site Type. |

### Borehole

A drilled hole used for subsurface investigation, sampling or monitoring. It is a
`SamplingLocation` and also has the fields of `GenericHole` and
`GeoDepthInterval`, both described below. Hole length may not exceed 12262 m, the length of the Kola
Superdeep Borehole.

Its depth interval must satisfy `bottom > top`, which the database enforces. A borehole that
breaks the rule is rejected on save. [How the depth interval fills itself
in](../explanation/how-the-depth-interval-fills-itself-in.md) explains how `top`, `bottom` and
`vertical_depth` relate.

## Rock samples

The `fairdm_geo.rocks` app (label `fairdm_geo_rocks`). Every rock sample model has the fields of
`BaseRock`, described below and a `specimen_type` field.

| Model | `specimen_type` starts as | Offered in forms |
|---|---|---|
| `RockSample` | `individualSample` | No |
| `DrillCore` | `core` | Yes |
| `DrillCuttings` | `cuttings` | No |
| `ThinSection` | `thinSection` | No |
| `RockPowder` | `rockPowder` | No |

`specimen_type` is a concept field drawing from ODM2 Specimen Type. Each starting value is the
concept with that name in the vocabulary.

### BaseRock

The abstract base of the rock sample models.

| Field | Type | Default | Description |
|---|---|---|---|
| `feature_type` | Concept | `http://vocabulary.odm2.org/samplingfeaturetype/specimen` | The kind of sampling feature the record describes. Vocabulary: ODM2 Sampling Feature Type. Not editable. |
| `medium` | Concept | `http://vocabulary.odm2.org/medium/rock` | The physical medium of the specimen. Vocabulary: ODM2 Medium. Not editable. |

## Stratigraphy

The `fairdm_geo.geology.stratigraphy` app (label `fairdm_geo_stratigraphy`).

### StratigraphicUnit

A body of rock recognised by its stratigraphic rank and how it formed. It is a plain Django model
and not a `Sample`.

| Field | Type | Default | Description |
|---|---|---|---|
| `rank` | Concept | None | The stratigraphic rank, such as formation or member. Vocabulary: CGI Stratigraphic Rank. Optional. |
| `genesis` | Concept | None | The geological process that formed the unit. Vocabulary: CGI Genetic Category. Optional. |

## Abstract base models

The `fairdm_geo.core` app (label `fairdm_geo_core`) holds the abstract models the concrete ones are
built from. Use them to build your own earth science samples.

### GenericEarthSample

The base of every earth science sample. It adds no fields to `Sample`.

### GenericHole

A field mixin for hole geometry. It is not a `Sample`, so a concrete model also inherits from
`GenericEarthSample` or another sample model. A subclass can set `HOLE_MAX_LENGTH`, in metres, and
validation then rejects a longer hole with the error code `hole_too_long`.

| Field | Type | Range | Description |
|---|---|---|---|
| `azimuth` | Quantity, degrees | 0 to 360 | The horizontal angle relative to a reference direction. Optional. |
| `inclination` | Quantity, degrees | 0 to 90 | The vertical angle relative to the horizontal plane, where 90 is true vertical. Optional. |
| `length` | Quantity, metres | 0 or more | The total length of the hole. Optional. |

### Interval

An abstract `GenericEarthSample` for the interval types. It adds no fields.

### VerticalInterval

A field mixin for a vertical interval defined by top and bottom measurements. Its database
constraint requires `bottom < top`.

| Field | Type | Default | Description |
|---|---|---|---|
| `top` | Quantity, metres | None | The distance to the top of the interval relative to the vertical datum. Optional. |
| `bottom` | Quantity, metres | None | The distance to the bottom of the interval relative to the vertical datum. Optional. |
| `vertical_depth` | Quantity, metres | None | The total depth of the interval. Optional. |
| `vertical_datum` | Text | `MSL` | The vertical datum. The only choice is `MSL` (Mean Sea Level). |

### VerticalDepthInterval

A `VerticalInterval` where measurements are positive downward. Its database constraint requires
`bottom > top` instead.

### GeoDepthInterval

A `VerticalDepthInterval` with lithology, age and stratigraphy.

| Field | Type | Description |
|---|---|---|
| `lithology` | Concepts | The lithology of the interval. Vocabulary: CGI Simple Lithology. Optional. |
| `age` | Concepts | The geologic age of the interval. Vocabulary: International Chronostratigraphic Chart 2020. Optional. |
| `stratigraphy` | Many-to-many to `StratigraphicUnit` | The stratigraphy of the interval. Optional. |

## Fields FairDM offers for each model

Each concrete model is registered with FairDM, which decides the fields its forms offer. The
registration is in the `config.py` module of each app.

| Model | Fields |
|---|---|
| `SamplingLocation` | `name`, `local_id`, `dataset`, `type`, `status`, `location`, `location_elevation` |
| `Borehole` | The fields of `SamplingLocation`, then `azimuth`, `inclination`, `length` |
| `RockSample` | `name`, `local_id`, `dataset`, `status`, `feature_type`, `medium`, `specimen_type` |
| `DrillCore` | `name`, `local_id`, `dataset`, `status`, `specimen_type` |
| `DrillCuttings` | `name`, `local_id`, `dataset`, `status` |
| `ThinSection` | `name`, `local_id`, `dataset`, `status` |
| `RockPowder` | `name`, `local_id`, `dataset`, `status` |

The `fairdm_geo.sites` app requires `fairdm_geo.core` to be installed, and raises
`ImproperlyConfigured` at startup if it is not. Listing `fairdm_geo` as an add-on installs it.
