"""Concrete rock sample models."""

from controlled_vocabularies.fields import ConceptField
from django.utils.translation import gettext_lazy as _

from fairdm_geo.vocabularies import (
    ODM2_SPECIMEN_TYPE,
    SPECIMEN_TYPE_CORE,
    SPECIMEN_TYPE_CUTTINGS,
    SPECIMEN_TYPE_INDIVIDUAL_SAMPLE,
    SPECIMEN_TYPE_ROCK_POWDER,
    SPECIMEN_TYPE_THIN_SECTION,
)

from .base import BaseRock


def specimen_type_field(default: str, *, editable: bool = False) -> ConceptField:
    """Build the specimen type field of a rock sample model.

    Args:
        default: URI of the concept the model starts with.
        editable: Whether a form offers the field.

    Returns:
        A concept field limited to the ODM2 specimen types.
    """
    return ConceptField(
        verbose_name=_("specimen"),
        help_text=_("The kind of specimen this record describes."),
        vocabulary=ODM2_SPECIMEN_TYPE,
        default=default,
        related_name="+",
        editable=editable,
    )


class RockSample(BaseRock):
    """A general rock specimen collected for geological analysis."""

    specimen_type = specimen_type_field(SPECIMEN_TYPE_INDIVIDUAL_SAMPLE)

    class Meta:
        abstract = False
        verbose_name = _("rock sample")
        verbose_name_plural = _("rock samples")


class DrillCore(BaseRock):
    """Core samples obtained from drilling operations."""

    specimen_type = specimen_type_field(SPECIMEN_TYPE_CORE, editable=True)

    class Meta:
        abstract = False
        verbose_name = _("drill core")
        verbose_name_plural = _("drill cores")


class DrillCuttings(BaseRock):
    """Rock fragments produced during drilling operations."""

    specimen_type = specimen_type_field(SPECIMEN_TYPE_CUTTINGS)

    class Meta:
        abstract = False
        verbose_name = _("drill cuttings")
        verbose_name_plural = _("drill cuttings")


class ThinSection(BaseRock):
    """Thin slices of rock mounted on glass slides for microscopic examination."""

    specimen_type = specimen_type_field(SPECIMEN_TYPE_THIN_SECTION)

    class Meta:
        abstract = False
        verbose_name = _("thin section")
        verbose_name_plural = _("thin sections")


class RockPowder(BaseRock):
    """Finely ground rock samples prepared for geochemical analysis."""

    specimen_type = specimen_type_field(SPECIMEN_TYPE_ROCK_POWDER)

    class Meta:
        abstract = False
        verbose_name = _("rock powder")
        verbose_name_plural = _("rock powders")
