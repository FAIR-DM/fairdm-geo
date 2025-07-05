from django.utils.translation import gettext as _
from fairdm.db import models
from research_vocabs.fields import ConceptManyToManyField

from fairdm_geo.vocabularies.cgi import geosciml
from fairdm_geo.vocabularies.stratigraphy import GeologicalTimescale

from .generic import GenericEarthSample

# ==============================
# NEED TO GO THROUGH AND CONVERT MOST OF THESE TO QUANTITY FIELDS
# ==============================


class Interval(GenericEarthSample):
    """"""

    # start = None
    # end = None
    # distance = None

    class Meta:
        abstract = True
        verbose_name = _("interval")
        verbose_name_plural = _("intervals")


class VerticalInterval(GenericEarthSample):
    # _metadata = Metadata(
    #     description=_(
    #         "A general vertical interval is a defined range within a vertical column, bounded by a top and bottom measurement, where both measurements are positive in the upward direction, relative to a specified reference point. This interval can span any physical medium, including air, water, or earth, and is used to represent a discrete section within that medium for the purpose of sampling, observation, or analysis. The vertical interval is characterized by its top and bottom boundaries, which define its extent, and can be further subclassed to create more specific data models tailored to particular scientific studies, such as soil horizons, water columns, or atmospheric layers."
    #     ),
    #     **default_metadata,
    # )

    top = models.QuantityField(
        base_units="m",
        verbose_name=_("top"),
        help_text=_("The distance to the top of the vertical interval relative to the vertical datum."),
        blank=True,
        null=True,
    )
    bottom = models.QuantityField(
        base_units="m",
        verbose_name=_("bottom"),
        help_text=_("The distance to the bottom of the vertical interval relative to the vertical datum."),
        blank=True,
        null=True,
    )

    # note: we cannot call this field "depth" because it clashes with the depth field used by django-treebeard
    # to create the MPTT tree structure.
    vertical_depth = models.QuantityField(
        base_units="m",
        verbose_name=_("vertical depth"),
        help_text=_(
            "The total depth of the vertical interval, calculated as the absolute difference between the interval top and interval bottom."
        ),
        blank=True,
        null=True,
    )

    vertical_datum = models.CharField(
        max_length=255,
        verbose_name=_("vertical datum"),
        help_text=_("The vertical datum used to determine depth measurements."),
        default="MSL",
        choices=[
            ("MSL", "Mean Sea Level"),
        ],
    )

    class Meta:
        abstract = True
        verbose_name = _("vertical interval")
        verbose_name_plural = _("vertical intervals")
        constraints = [
            models.CheckConstraint(
                condition=models.Q(bottom__lt=models.F("top")),
                name="top_above_bottom_upward",
            )
        ]

    def save(self, *args, **kwargs):
        if self.top is not None and self.bottom is not None:
            self.vertical_depth = abs(self.bottom - self.top)
        elif self.top is not None and self.vertical_depth is not None:
            # If only top and vertical_depth are provided, calculate bottom
            self.bottom = self.top + self.vertical_depth
        elif self.bottom is not None and self.vertical_depth is not None:
            # If only bottom and vertical_depth are provided, calculate top
            self.top = self.bottom - self.vertical_depth
        elif self.top is None and self.bottom is None and self.vertical_depth is not None:
            # If only vertical_depth is provided, set top to 0 and calculate bottom
            self.top = 0
            self.bottom = self.vertical_depth
        super().save(*args, **kwargs)


class VerticalDepthInterval(VerticalInterval):
    """A vertical interval where measurements are positive in the downward direction."""

    class Meta:
        abstract = True
        verbose_name = _("depth interval")
        verbose_name_plural = _("depth intervals")
        # NOTE: The constraint has changed from bottom__lt to bottom__gt because the measurements are
        # positive in the downward direction.
        constraints = [
            models.CheckConstraint(
                check=models.Q(bottom__gt=models.F("top")),
                name="top_above_bottom",
            )
        ]


class GeoDepthInterval(VerticalDepthInterval):
    lithology = ConceptManyToManyField(
        vocabulary=geosciml.SimpleLithology,
        verbose_name=_("lithology"),
        help_text=_("The lithology of the interval."),
        blank=True,
    )
    # age = models.ManyToManyField(
    # "geologic_time.GeologicalTimescale",
    age = ConceptManyToManyField(
        vocabulary=GeologicalTimescale,
        verbose_name=_("geologic age"),
        help_text=_("The geologic age of the interval."),
        blank=True,
    )
    stratigraphy = models.ManyToManyField(
        "stratigraphy.StratigraphicUnit",
        verbose_name=_("stratigraphy"),
        help_text=_("The stratigraphy of the interval."),
        blank=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("geological depth interval")
        verbose_name_plural = _("geological depth intervals")
