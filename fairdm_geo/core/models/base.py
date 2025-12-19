"""Abstract base models for earth science samples and intervals."""

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from fairdm.core.models import Sample
from fairdm.db import models
from research_vocabs.fields import ConceptManyToManyField

from fairdm_geo.vocabularies.cgi import geosciml
from fairdm_geo.vocabularies.stratigraphy import GeologicalTimescale


class GenericEarthSample(Sample):
    """Abstract base class for all earth science samples."""

    class Meta:
        abstract = True
        verbose_name = _("generic earth sample")
        verbose_name_plural = _("generic earth samples")


class GenericHole(GenericEarthSample):
    """
    A generic hole is a sample type created when drilling/probing into another sample,
    typically for the purpose of creating child samples. Use this abstract model in order
    to record information about how certain samples were collected.
    E.g. samples from a borehole.
    """

    HOLE_MAX_LENGTH = None

    azimuth = models.QuantityField(
        base_units="deg",
        verbose_name=_("azimuth"),
        help_text=_("The horizontal angle relative to a reference direction."),
        validators=[MinValueValidator(0), MaxValueValidator(360)],
        blank=True,
        null=True,
    )
    inclination = models.QuantityField(
        base_units="deg",
        verbose_name=_("inclination"),
        help_text=_("The vertical angle relative to the horizontal plane where 90 is true vertical."),
        validators=[MinValueValidator(0), MaxValueValidator(90)],
        blank=True,
        null=True,
    )
    length = models.QuantityField(
        base_units="m",
        verbose_name=_("hole length"),
        help_text=_("The total length of the hole."),
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("hole")
        verbose_name_plural = _("holes")

    def clean(self):
        """Validate that hole length doesn't exceed maximum if defined."""
        if self.length and self.HOLE_MAX_LENGTH and self.length.magnitude > self.HOLE_MAX_LENGTH:
            msg = f"Length of hole ({self.length}) exceeds maximum length ({self.HOLE_MAX_LENGTH} m)."
            raise ValidationError(msg)
        super().clean()


# ==============================
# Interval Models
# ==============================


class Interval(GenericEarthSample):
    """Abstract base class for all interval types."""

    class Meta:
        abstract = True
        verbose_name = _("interval")
        verbose_name_plural = _("intervals")


class VerticalInterval(GenericEarthSample):
    """
    A general vertical interval is a defined range within a vertical column, bounded by a
    top and bottom measurement, where both measurements are positive in the upward direction,
    relative to a specified reference point. This interval can span any physical medium,
    including air, water, or earth, and is used to represent a discrete section within that
    medium for the purpose of sampling, observation, or analysis.
    """

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
        """Automatically calculate missing depth values from provided values."""
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
    """A geological depth interval with lithology, age, and stratigraphy information."""

    lithology = ConceptManyToManyField(
        vocabulary=geosciml.SimpleLithology,
        verbose_name=_("lithology"),
        help_text=_("The lithology of the interval."),
        blank=True,
    )
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
