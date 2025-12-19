"""
Model Configuration for Sampling Locations

This module registers all sampling location models with the FairDM framework
using the modern @register decorator and ModelConfiguration system.
"""

from django.utils.translation import gettext_lazy as _
from fairdm import register
from fairdm.registry import Authority, ModelConfiguration, ModelMetadata

from fairdm_geo.sites.models import Borehole, SamplingLocation

# Shared authority for all FairDM Geo models
GEO_AUTHORITY = Authority(
    name="FairDM Geo Development Team",
    short_name="FairDM Geo",
    website="https://github.com/FAIR-DM/fairdm-geo",
)


@register
class SamplingLocationConfig(ModelConfiguration):
    """Configuration for geographic sampling locations."""

    model = SamplingLocation

    metadata = ModelMetadata(
        description=_(
            "A sampling location represents a specific geographic point where samples are collected. "
            "Includes precise coordinates, elevation data, and site characteristics that enable "
            "reproducible sampling and accurate data interpretation within geographical context."
        ),
        authority=GEO_AUTHORITY,
        keywords=["geography", "sampling", "location", "site", "coordinates"],
    )

    fields = [
        "name",
        "local_id",
        "dataset",
        "type",
        "status",
        "location",
        "latitude",
        "longitude",
        "elevation",
        "elevation_datum",
    ]

    exclude = ["polymorphic_ctype"]


@register
class BoreholeConfig(ModelConfiguration):
    """Configuration for borehole sampling features."""

    model = Borehole

    metadata = ModelMetadata(
        description=_(
            "A borehole represents a drilled hole in the ground used for subsurface investigation, "
            "sampling, or monitoring. Includes detailed geometry (azimuth, inclination, length) "
            "and serves as a container for depth-based sampling and measurements."
        ),
        authority=GEO_AUTHORITY,
        keywords=["geology", "drilling", "borehole", "subsurface", "well"],
    )

    fields = [
        "name",
        "local_id",
        "dataset",
        "type",
        "status",
        "location",
        "latitude",
        "longitude",
        "elevation",
        "elevation_datum",
        "azimuth",
        "inclination",
        "length",
    ]

    exclude = ["polymorphic_ctype"]
