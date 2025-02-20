from django.utils.translation import gettext as _
from research_vocabs.fields import ConceptField

from fairdm_geo.utils import is_abstract
from fairdm_geo.vocabularies.odm2 import Medium, SamplingFeatureType, SpecimenType

from .generic import GenericEarthSample


class BaseRock(GenericEarthSample):
    feature_type = ConceptField(
        vocabulary=SamplingFeatureType,
        default="specimen",
        editable=False,
    )
    medium = ConceptField(
        verbose_name=_("medium"),
        vocabulary=Medium,
        default="rock",
        editable=False,
    )

    class Meta:
        abstract = True


class RockSample(BaseRock):
    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="individualSample",
        editable=False,
    )

    class Meta:
        abstract = is_abstract("RockSample")
        verbose_name = _("rock sample")
        verbose_name_plural = _("rock samples")


class DrillCore(BaseRock):
    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        # from_members=[
        #     "core",
        #     "coreHalfRound",
        #     "corePiece",
        #     "coreQuarterRound",
        #     "coreSection",
        #     "coreSectionHalf",
        #     "coreSub-Piece",
        #     "coreWholeRound",
        #     "cuttings",
        #     "orientedCore",
        # ],
        default="core",
    )

    class Meta:
        abstract = is_abstract("DrillCore")
        verbose_name = _("drill core")
        verbose_name_plural = _("drill cores")


class DrillCuttings(BaseRock):
    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="cuttings",
        editable=False,
    )

    class Meta:
        abstract = is_abstract("DrillCuttings")
        verbose_name = _("rock sample")
        verbose_name_plural = _("rock samples")


class ThinSection(BaseRock):
    ALLOWED_PARENTS = ["fairdm_geo.RockSample"]

    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="thinSection",
        editable=False,
    )

    class Meta:
        abstract = is_abstract("ThinSection")
        verbose_name = _("thin section")
        verbose_name_plural = _("thin sections")


class RockPowder(BaseRock):
    ALLOWED_PARENTS = ["RockSample"]

    specimen_type = ConceptField(
        verbose_name=_("specimen"),
        vocabulary=SpecimenType,
        default="powder",
        editable=False,
    )

    class Meta:
        abstract = is_abstract("RockPowder")
        verbose_name = _("rock powder")
        verbose_name_plural = _("rock powders")
