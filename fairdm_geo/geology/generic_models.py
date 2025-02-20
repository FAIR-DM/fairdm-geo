from django.utils.translation import gettext as _
from research_vocabs.fields import ConceptField

from fairdm_geo.models.samples.generic import GenericEarthSample
from fairdm_geo.vocabularies.cgi import geosciml


class GenericCompoundMaterial(GenericEarthSample):
    _defaults = {}

    consolidation_degree = ConceptField(
        concept_class=geosciml.ConsolidationDegree,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Compound Material")
        verbose_name_plural = _("Compound Materials")


class GenericRock(GenericEarthSample):
    """This is an abstract model for a generic rock sample that includes several controlled vocabulary fields based
    on the CGI geosciml vocabulary. It is intended to be subclassed to create specific rock types. Before using, take
    a look at the pre-defined sample types available in fairdm_geo.geology.rock_samples to see if any fit your needs."""

    class Meta:
        abstract = True
        verbose_name = _("Generic Rock")
        verbose_name_plural = _("Generic Rocks")
