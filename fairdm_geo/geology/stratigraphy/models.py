from django.db import models
from django.utils.translation import gettext as _
from research_vocabs.fields import ConceptField

from fairdm_geo.vocabularies.cgi import geosciml


class StratigraphicUnit(models.Model):
    _defaults = {}

    rank = ConceptField(
        vocabulary=geosciml.StratigraphicRank,
        blank=True,
        null=True,
    )

    genesis = ConceptField(
        vocabulary=geosciml.GeneticCategory,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Stratigraphic Unit")
        verbose_name_plural = _("Stratigraphic Units")

    def save(self, *args, **kwargs):
        # make sure the rank of the unit is not equal to or greater than the rank of the parent unit
        if self.parent and self.rank and self.parent.rank and self.rank >= self.parent.rank:
            raise ValueError(_("The rank of the unit must be less than the rank of the parent unit"))

        super().save(*args, **kwargs)
