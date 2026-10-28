"""The published vocabularies that fairdm_geo's model fields draw their concepts from.

Each file ships inside the package, so ``manage.py sync_vocabularies`` never needs the
network. ``README.md`` beside this module gives the source and licence of every file.
"""

from pathlib import Path

from controlled_vocabularies.fields import Vocabulary

FILES = Path(__file__).parent

ODM2_MEDIUM = Vocabulary(
    "http://vocabulary.odm2.org/medium",
    source=FILES / "odm2" / "medium.rdf",
)
ODM2_SAMPLING_FEATURE_TYPE = Vocabulary(
    "http://vocabulary.odm2.org/samplingfeaturetype",
    source=FILES / "odm2" / "samplingfeaturetype.rdf",
)
ODM2_SITE_TYPE = Vocabulary(
    "http://vocabulary.odm2.org/sitetype",
    source=FILES / "odm2" / "sitetype.rdf",
)
ODM2_SPECIMEN_TYPE = Vocabulary(
    "http://vocabulary.odm2.org/specimentype",
    source=FILES / "odm2" / "specimentype.rdf",
)

CGI_GENETIC_CATEGORY = Vocabulary(
    "http://resource.geosciml.org/classifierscheme/cgi/2016.01/geneticcategory",
    source=FILES / "cgi" / "geneticcategory.ttl",
)
CGI_SIMPLE_LITHOLOGY = Vocabulary(
    "http://resource.geosciml.org/classifierscheme/cgi/2016.01/simplelithology",
    source=FILES / "cgi" / "simplelithology.ttl",
)
CGI_STRATIGRAPHIC_RANK = Vocabulary(
    "http://resource.geosciml.org/classifierscheme/cgi/2016.01/stratigraphicrank",
    source=FILES / "cgi" / "stratigraphicrank.ttl",
)

ICS_TIMESCALE = Vocabulary(
    "http://resource.geosciml.org/vocabulary/timescale/gts2020",
    source=FILES / "ics" / "isc2020.ttl",
)

#: The concept each model field starts with, by URI.
MEDIUM_ROCK = f"{ODM2_MEDIUM.uri}/rock"
SAMPLING_FEATURE_SPECIMEN = f"{ODM2_SAMPLING_FEATURE_TYPE.uri}/specimen"
SITE_TYPE_UNKNOWN = f"{ODM2_SITE_TYPE.uri}/unknown"
SPECIMEN_TYPE_CORE = f"{ODM2_SPECIMEN_TYPE.uri}/core"
SPECIMEN_TYPE_CUTTINGS = f"{ODM2_SPECIMEN_TYPE.uri}/cuttings"
SPECIMEN_TYPE_INDIVIDUAL_SAMPLE = f"{ODM2_SPECIMEN_TYPE.uri}/individualSample"
SPECIMEN_TYPE_ROCK_POWDER = f"{ODM2_SPECIMEN_TYPE.uri}/rockPowder"
SPECIMEN_TYPE_THIN_SECTION = f"{ODM2_SPECIMEN_TYPE.uri}/thinSection"
