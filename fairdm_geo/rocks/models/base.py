"""Base rock model."""

from django.utils.translation import gettext as _
from research_vocabs.fields import ConceptField

from fairdm_geo.core.models import GenericEarthSample
from fairdm_geo.vocabularies.odm2 import Medium, SamplingFeatureType, SpecimenType


class BaseRock(GenericEarthSample):
    """Abstract base class for all rock sample types."""

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
