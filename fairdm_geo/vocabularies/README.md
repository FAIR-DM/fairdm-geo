# Shipped vocabularies

Every file below is a published SKOS vocabulary, kept unmodified so loading never needs the
network. A model field names a vocabulary in `fairdm_geo/vocabularies/__init__.py`, and
`manage.py sync_vocabularies` loads the file.

All files were retrieved on 2026-10-28.

| File | Vocabulary | Source | Licence |
|---|---|---|---|
| `odm2/medium.rdf` | ODM2 Medium | <http://vocabulary.odm2.org/api/v1/medium/?format=skos> | See below |
| `odm2/samplingfeaturetype.rdf` | ODM2 Sampling Feature Type | <http://vocabulary.odm2.org/api/v1/samplingfeaturetype/?format=skos> | See below |
| `odm2/sitetype.rdf` | ODM2 Site Type | <http://vocabulary.odm2.org/api/v1/sitetype/?format=skos> | See below |
| `odm2/specimentype.rdf` | ODM2 Specimen Type | <http://vocabulary.odm2.org/api/v1/specimentype/?format=skos> | See below |
| `cgi/geneticcategory.ttl` | CGI GeoSciML Genetic Category | <https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/geneticcategory.ttl> | CC BY 4.0 |
| `cgi/simplelithology.ttl` | CGI GeoSciML Simple Lithology | <https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/simplelithology.ttl> | CC BY 4.0 |
| `cgi/stratigraphicrank.ttl` | CGI GeoSciML Stratigraphic Rank | <https://raw.githubusercontent.com/CGI-IUGS/cgi-vocabs/master/vocabularies/geosciml/stratigraphicrank.ttl> | CC BY 4.0 |
| `ics/isc2020.ttl` | International Chronostratigraphic Chart 2020 (Geologic Time Scale) | <https://vocabs.ardc.edu.au/registry/api/resource/downloads/1211/isc2020.ttl> | CC BY 4.0, stated in the file |

The CGI licence is the one the [CGI-IUGS vocabularies repository](https://github.com/CGI-IUGS/cgi-vocabs/blob/master/LICENSE)
declares. The ODM2 files state no licence of their own. The
[ODM2 project](https://github.com/ODM2/ODM2/blob/master/LICENSE) publishes its source under a
BSD-style licence from the Consortium of Universities for the Advancement of Hydrologic Science.
