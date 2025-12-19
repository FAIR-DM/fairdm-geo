"""Concrete rock sample models."""

from django.utils.translation import gettext as _
from research_vocabs.fields import ConceptField

from fairdm_geo.vocabularies.odm2 import SpecimenType

from .base import BaseRock


class RockSample(BaseRock):
    """A general rock specimen collected for geological analysis."""

    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="individualSample",
        editable=False,
    )

    class Meta:
        abstract = False
        verbose_name = _("rock sample")
        verbose_name_plural = _("rock samples")


class DrillCore(BaseRock):
    """Core samples obtained from drilling operations."""

    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="core",
    )

    class Meta:
        abstract = False
        verbose_name = _("drill core")
        verbose_name_plural = _("drill cores")


class DrillCuttings(BaseRock):
    """Rock fragments produced during drilling operations."""

    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="cuttings",
        editable=False,
    )

    class Meta:
        abstract = False
        verbose_name = _("drill cuttings")
        verbose_name_plural = _("drill cuttings")


class ThinSection(BaseRock):
    """Thin slices of rock mounted on glass slides for microscopic examination."""

    ALLOWED_PARENTS = ["fairdm_geo.RockSample"]

    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="thinSection",
        editable=False,
    )

    class Meta:
        abstract = False
        verbose_name = _("thin section")
        verbose_name_plural = _("thin sections")


class RockPowder(BaseRock):
    """Finely ground rock samples prepared for geochemical analysis."""

    ALLOWED_PARENTS = ["RockSample"]

    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="powder",
        editable=False,
    )

    class Meta:
        abstract = False
        verbose_name = _("rock powder")
        verbose_name_plural = _("rock powders")
