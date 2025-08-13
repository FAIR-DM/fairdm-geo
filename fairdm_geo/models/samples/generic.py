from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from fairdm.core.models import Sample
from fairdm.db import models


class GenericEarthSample(Sample):
    class Meta:
        abstract = True
        verbose_name = _("generic earth sample")
        verbose_name_plural = _("generic earth samples")


class GenericHole(GenericEarthSample):
    """A generic hole is a sample type created when drilling/probing into another sample, typically for the purpose of creating child
    samples. Use this abstract model in order to record information about how certain samples were collected.
    E.g. samples from a borehole."""

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
        if self.length:
            if self.HOLE_MAX_LENGTH and self.length.magnitude > self.HOLE_MAX_LENGTH:
                raise ValidationError(
                    f"Length of hole ({self.length}) exceeds maximum length ({self.HOLE_MAX_LENGTH} m)."
                )
        super().clean()
