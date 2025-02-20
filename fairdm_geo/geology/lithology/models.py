from django.db import models
from django.utils.translation import gettext as _
from fairdm_geo.vocabularies.cgi import geosciml
from research_vocabs.models import AbstractConcept


class SimpleLithology(AbstractConcept):
    vocabulary_name = None
    _vocabulary = geosciml.SimpleLithology()
    name = models.CharField(_("name"), max_length=255, unique=True, primary_key=True)

    class Meta:
        verbose_name = _("Simple Lithology")
        verbose_name_plural = _("Simple Lithology")

    def __str__(self):
        return f"{self.label}"

    # @classmethod
    # def _get_defaults(cls, concept):
    #     defaults = super()._get_defaults(concept)

    #     comments = concept.attrs.get("rdfs:comment", [])

    #     if not comments:
    #         return defaults

    #     if not isinstance(comments, list):
    #         comments = [comments]

    #     for c in comments:
    #         defaults.update(cls._parse_age_comment(c))

    #     return defaults


# class StratigraphicBoundary(AbstractConcept):
#     vocabulary_name = None
#     _vocabulary = StratigraphicBoundary()

#     class Meta:
#         verbose_name = _("Stratigraphic Boundary")
#         verbose_name_plural = _("Stratigraphic Boundaries")
