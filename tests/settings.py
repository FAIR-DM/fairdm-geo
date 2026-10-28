"""Settings for the test suite: a FairDM portal with every fairdm_geo app installed."""

from pathlib import Path

import fairdm

# Read before ``setup()``, which rebinds ``__file__`` while it applies each settings layer.
VOCABULARY_FILES = Path(__file__).resolve().parent / "fixtures" / "vocabularies"

fairdm.setup(
    apps=[
        "fairdm_geo.sites",
        "fairdm_geo.rocks",
    ],
    addons=["fairdm_geo"],
)

ROOT_URLCONF = "fairdm.conf.urls"

# FairDM's own vocabularies, copied from the FairDM 0.3.0 test fixtures so the suite
# never fetches them over the network.
CONTROLLED_VOCABULARIES = {
    slug: {"source": VOCABULARY_FILES / f"{slug}.ttl"}
    for slug in (
        "contributor-roles",
        "date-types",
        "description-types",
        "identifier-types",
        "organization-types",
        "project-status",
        "relation-types",
        "sample-relation-types",
        "sample-status",
    )
}
