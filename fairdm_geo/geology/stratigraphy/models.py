"""Models for stratigraphic units."""

from controlled_vocabularies.fields import ConceptField
from django.db import models
from django.utils.translation import gettext_lazy as _

from fairdm_geo.vocabularies import CGI_GENETIC_CATEGORY, CGI_STRATIGRAPHIC_RANK


class StratigraphicUnit(models.Model):
    """A body of rock recognised by its stratigraphic rank and how it formed."""

    rank = ConceptField(
        vocabulary=CGI_STRATIGRAPHIC_RANK,
        verbose_name=_("rank"),
        help_text=_("The stratigraphic rank of the unit, such as formation or member."),
        related_name="+",
        blank=True,
        null=True,
    )

    genesis = ConceptField(
        vocabulary=CGI_GENETIC_CATEGORY,
        verbose_name=_("genesis"),
        help_text=_("The geological process that formed the unit."),
        related_name="+",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Stratigraphic Unit")
        verbose_name_plural = _("Stratigraphic Units")
