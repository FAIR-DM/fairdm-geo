"""
Model Configuration for FairDM Geo

This module registers all geoscience-specific Sample models with the FairDM framework
using the modern @register decorator and ModelConfiguration system.

Each configuration defines:
- Model metadata (description, authority, keywords)
- Table display fields
- Form fields for create/edit
- Filter fields for list views
"""

from django.utils.translation import gettext_lazy as _
from fairdm import register
from fairdm.registry import Authority, ModelConfiguration, ModelMetadata

# Import all geoscience models
from fairdm_geo.models.features import Borehole, SamplingLocation
from fairdm_geo.models.samples import (
    DrillCore,
    DrillCuttings,
    RockPowder,
    RockSample,
    ThinSection,
)

# Shared authority for all FairDM Geo models
GEO_AUTHORITY = Authority(
    name="FairDM Geo Development Team",
    short_name="FairDM Geo",
    website="https://github.com/FAIR-DM/fairdm-geo",
)


# =============================================================================
# Rock Sample Configurations
# =============================================================================


@register
class RockSampleConfig(ModelConfiguration):
    """Configuration for general rock specimens."""

    model = RockSample

    metadata = ModelMetadata(
        description=_(
            "Rock specimens collected for geological analysis. Includes information about "
            "the sample's physical characteristics, collection location, and geological context."
        ),
        authority=GEO_AUTHORITY,
        keywords=["geology", "rock", "specimen", "petrology"],
    )

    fields = [
        "name",
        "local_id",
        "dataset",
        "status",
        "feature_type",
        "medium",
        "specimen_type",
        "parent",
    ]

    exclude = ["polymorphic_ctype"]


@register
class DrillCoreConfig(ModelConfiguration):
    """Configuration for drill core samples."""

    model = DrillCore

    metadata = ModelMetadata(
        description=_(
            "Core samples obtained from drilling operations. Includes whole cores, core sections, "
            "and oriented cores with detailed stratigraphic and structural information."
        ),
        authority=GEO_AUTHORITY,
        keywords=["geology", "drilling", "core", "stratigraphy"],
    )

    fields = [
        "name",
        "local_id",
        "dataset",
        "status",
        "specimen_type",
        "parent",
    ]

    exclude = ["polymorphic_ctype", "feature_type", "medium"]


@register
class DrillCuttingsConfig(ModelConfiguration):
    """Configuration for drill cuttings samples."""

    model = DrillCuttings

    metadata = ModelMetadata(
        description=_(
            "Rock fragments produced during drilling operations. Typically collected at regular "
            "intervals to provide continuous geological information along the borehole."
        ),
        authority=GEO_AUTHORITY,
        keywords=["geology", "drilling", "cuttings", "borehole"],
    )

    fields = [
        "name",
        "local_id",
        "dataset",
        "status",
        "parent",
    ]

    exclude = ["polymorphic_ctype", "feature_type", "medium", "specimen_type"]


@register
class ThinSectionConfig(ModelConfiguration):
    """Configuration for thin section samples."""

    model = ThinSection

    metadata = ModelMetadata(
        description=_(
            "Thin slices of rock mounted on glass slides for microscopic examination. "
            "Essential for petrographic analysis and mineral identification."
        ),
        authority=GEO_AUTHORITY,
        keywords=["geology", "petrography", "microscopy", "thin section"],
    )

    fields = [
        "name",
        "local_id",
        "dataset",
        "status",
        "parent",
    ]

    exclude = ["polymorphic_ctype", "feature_type", "medium", "specimen_type"]


@register
class RockPowderConfig(ModelConfiguration):
    """Configuration for powdered rock samples."""

    model = RockPowder

    metadata = ModelMetadata(
        description=_(
            "Finely ground rock samples prepared for geochemical analysis. "
            "Used for techniques such as XRF, ICP-MS, and isotopic studies."
        ),
        authority=GEO_AUTHORITY,
        keywords=["geology", "geochemistry", "powder", "analysis"],
    )

    fields = [
        "name",
        "local_id",
        "dataset",
        "status",
        "parent",
    ]

    exclude = ["polymorphic_ctype", "feature_type", "medium", "specimen_type"]


# =============================================================================
# Sampling Feature Configurations
# =============================================================================


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
