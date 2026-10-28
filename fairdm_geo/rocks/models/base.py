"""Base rock model."""

from controlled_vocabularies.fields import ConceptField
from django.utils.translation import gettext_lazy as _

from fairdm_geo.core.models import GenericEarthSample
from fairdm_geo.vocabularies import (
    MEDIUM_ROCK,
    ODM2_MEDIUM,
    ODM2_SAMPLING_FEATURE_TYPE,
    SAMPLING_FEATURE_SPECIMEN,
)


class BaseRock(GenericEarthSample):
    """Abstract base class for all rock sample types."""

    feature_type = ConceptField(
        verbose_name=_("feature type"),
        help_text=_("The kind of sampling feature this record describes."),
        vocabulary=ODM2_SAMPLING_FEATURE_TYPE,
        default=SAMPLING_FEATURE_SPECIMEN,
        related_name="+",
        editable=False,
    )
    medium = ConceptField(
        verbose_name=_("medium"),
        help_text=_("The physical medium of the specimen."),
        vocabulary=ODM2_MEDIUM,
        default=MEDIUM_ROCK,
        related_name="+",
        editable=False,
    )

    class Meta:
        abstract = True
