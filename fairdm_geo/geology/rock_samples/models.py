from django.utils.translation import gettext as _
from research_vocabs.fields import ConceptField

from fairdm_geo.geology.generic_models import GenericRock
from fairdm_geo.models.samples.generic import GenericEarthSample
from fairdm_geo.vocabularies.cgi import geosciml


class CompoundMaterial(GenericEarthSample):
    _defaults = {}
    vocabulary = None

    # I guess this probably needs to be a relationship to a new model
    constituent_parts = ConceptField(
        concept_class=geosciml.CompoundMaterialConstituentPart,
        blank=True,
        null=True,
    )

    consolidation_degree = ConceptField(
        concept_class=geosciml.ConsolidationDegree,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Compound Material")
        verbose_name_plural = _("Compound Materials")


class Rock(GenericRock):
    _defaults = {}

    alteration_type = ConceptField(
        concept_class=geosciml.AlterationType,
        blank=True,
        null=True,
    )

    composition_category = ConceptField(
        concept_class=geosciml.CompositionCategory,
        blank=True,
        null=True,
    )

    lineation = ConceptField(
        concept_class=geosciml.Lineation,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Rock")
        verbose_name_plural = _("Rocks")

    def save(self, *args, **kwargs):
        # assign any default values that are not already set
        for field, value in self._defaults.items():
            if not getattr(self, field):
                setattr(self, field, value)
        super().save(*args, **kwargs)
