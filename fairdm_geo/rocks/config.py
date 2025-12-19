"""
Model Configuration for Rock Samples

This module registers all rock sample models with the FairDM framework
using the modern @register decorator and ModelConfiguration system.
"""

from django.utils.translation import gettext_lazy as _
from fairdm import register
from fairdm.registry import Authority, ModelConfiguration, ModelMetadata

from fairdm_geo.rocks.models import DrillCore, DrillCuttings, RockPowder, RockSample, ThinSection

# Shared authority for all FairDM Geo models
GEO_AUTHORITY = Authority(
    name="FairDM Geo Development Team",
    short_name="FairDM Geo",
    website="https://github.com/FAIR-DM/fairdm-geo",
)


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
