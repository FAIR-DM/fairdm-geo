# Vocabularies

The published vocabularies the models draw their terms from. Each is a SKOS file kept unmodified in
`fairdm_geo/vocabularies/`, and the module of the same name declares it. The
[vocabularies README](https://github.com/FAIR-DM/fairdm-geo/blob/main/fairdm_geo/vocabularies/README.md)
gives the download address, retrieval date and licence of every file.

| Vocabulary | Publisher | Used by | File |
|---|---|---|---|
| ODM2 Elevation Datum | ODM2 | `SamplingLocation.elevation_datum` | `odm2/elevationdatum.rdf` |
| ODM2 Medium | ODM2 | `BaseRock.medium` | `odm2/medium.rdf` |
| ODM2 Sampling Feature Type | ODM2 | `BaseRock.feature_type` | `odm2/samplingfeaturetype.rdf` |
| ODM2 Site Type | ODM2 | `SamplingLocation.type` | `odm2/sitetype.rdf` |
| ODM2 Specimen Type | ODM2 | `specimen_type` on each rock sample model | `odm2/specimentype.rdf` |
| CGI GeoSciML Genetic Category | CGI-IUGS | `StratigraphicUnit.genesis` | `cgi/geneticcategory.ttl` |
| CGI GeoSciML Simple Lithology | CGI-IUGS | `GeoDepthInterval.lithology` | `cgi/simplelithology.ttl` |
| CGI GeoSciML Stratigraphic Rank | CGI-IUGS | `StratigraphicUnit.rank` | `cgi/stratigraphicrank.ttl` |
| International Chronostratigraphic Chart 2020 | ICS | `GeoDepthInterval.age` | `ics/isc2020.ttl` |

## Vocabulary URIs

The URI is what a field stores to identify the vocabulary.

| Name in `fairdm_geo.vocabularies` | URI |
|---|---|
| `ODM2_ELEVATION_DATUM` | `http://vocabulary.odm2.org/elevationdatum` |
| `ODM2_MEDIUM` | `http://vocabulary.odm2.org/medium` |
| `ODM2_SAMPLING_FEATURE_TYPE` | `http://vocabulary.odm2.org/samplingfeaturetype` |
| `ODM2_SITE_TYPE` | `http://vocabulary.odm2.org/sitetype` |
| `ODM2_SPECIMEN_TYPE` | `http://vocabulary.odm2.org/specimentype` |
| `CGI_GENETIC_CATEGORY` | `http://resource.geosciml.org/classifierscheme/cgi/2016.01/geneticcategory` |
| `CGI_SIMPLE_LITHOLOGY` | `http://resource.geosciml.org/classifierscheme/cgi/2016.01/simplelithology` |
| `CGI_STRATIGRAPHIC_RANK` | `http://resource.geosciml.org/classifierscheme/cgi/2016.01/stratigraphicrank` |
| `ICS_TIMESCALE` | `http://resource.geosciml.org/vocabulary/timescale/gts2020` |

## Starting concepts

The module also names the concept each field starts with. Each is the vocabulary's URI followed by
the concept's name.

| Name in `fairdm_geo.vocabularies` | Concept |
|---|---|
| `ELEVATION_DATUM_MSL` | `http://vocabulary.odm2.org/elevationdatum/MSL` |
| `MEDIUM_ROCK` | `http://vocabulary.odm2.org/medium/rock` |
| `SAMPLING_FEATURE_SPECIMEN` | `http://vocabulary.odm2.org/samplingfeaturetype/specimen` |
| `SITE_TYPE_UNKNOWN` | `http://vocabulary.odm2.org/sitetype/unknown` |
| `SPECIMEN_TYPE_CORE` | `http://vocabulary.odm2.org/specimentype/core` |
| `SPECIMEN_TYPE_CUTTINGS` | `http://vocabulary.odm2.org/specimentype/cuttings` |
| `SPECIMEN_TYPE_INDIVIDUAL_SAMPLE` | `http://vocabulary.odm2.org/specimentype/individualSample` |
| `SPECIMEN_TYPE_ROCK_POWDER` | `http://vocabulary.odm2.org/specimentype/rockPowder` |
| `SPECIMEN_TYPE_THIN_SECTION` | `http://vocabulary.odm2.org/specimentype/thinSection` |

## Licences

The CGI vocabularies are licensed CC BY 4.0, and the International Chronostratigraphic Chart file
states CC BY 4.0. The ODM2 files state no licence of their own. The README linked above explains
where each licence comes from.
