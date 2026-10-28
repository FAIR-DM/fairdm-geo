"""Concrete sampling location and borehole models."""

from controlled_vocabularies.fields import ConceptField
from django.utils.translation import gettext as _
from fairdm.db.models import QuantityField

from fairdm_geo.core.models import GenericEarthSample, GenericHole, GeoDepthInterval
from fairdm_geo.vocabularies import (
    ELEVATION_DATUM_MSL,
    ODM2_ELEVATION_DATUM,
    ODM2_SITE_TYPE,
    SITE_TYPE_UNKNOWN,
)


class SamplingLocation(GenericEarthSample):
    """A sampling location represents a specific geographic point where samples are collected.

    Includes precise coordinates, elevation data, and site characteristics that enable
    reproducible sampling and accurate data interpretation within geographical context.
    """

    icon = "location"

    type = ConceptField(
        vocabulary=ODM2_SITE_TYPE,
        default=SITE_TYPE_UNKNOWN,
        related_name="+",
        verbose_name=_("type"),
        help_text=_("The type of sampling location."),
    )

    elevation_datum = ConceptField(
        verbose_name=_("elevation datum"),
        help_text=_(
            "The reference point for the elevation measurement, such as Mean Sea Level (MSL)."
        ),
        vocabulary=ODM2_ELEVATION_DATUM,
        default=ELEVATION_DATUM_MSL,
        related_name="+",
    )

    elevation = QuantityField(
        verbose_name=_("elevation"),
        base_units="m",
        unit_choices=["m", "ft"],
        null=True,
        blank=True,
        help_text=_(
            "The site elevation in meters with reference to the specified elevation datum."
        ),
    )

    class Meta:
        abstract = False
        verbose_name = _("sampling location")
        verbose_name_plural = _("sampling locations")


class Borehole(GeoDepthInterval, GenericHole, SamplingLocation):
    """A drilled hole in the ground used for subsurface investigation, sampling or monitoring.

    Includes detailed geometry (azimuth, inclination, length) and serves as a container for
    depth-based sampling and measurements.
    """

    HOLE_MAX_LENGTH = 12262  # meters (Kola Superdeep Borehole)

    class Meta(GeoDepthInterval.Meta):
        abstract = False
        verbose_name = _("borehole")
        verbose_name_plural = _("boreholes")
