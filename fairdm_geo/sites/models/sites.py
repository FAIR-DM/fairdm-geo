"""Concrete sampling location and borehole models."""

from controlled_vocabularies.fields import ConceptField
from django.utils.translation import gettext_lazy as _

from fairdm_geo.core.models import GenericEarthSample, GenericHole, GeoDepthInterval
from fairdm_geo.vocabularies import (
    ODM2_SITE_TYPE,
    SITE_TYPE_UNKNOWN,
)


class SamplingLocation(GenericEarthSample):
    """A sampling location represents a specific geographic point where samples are collected.

    Includes precise coordinates and site characteristics that enable
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
