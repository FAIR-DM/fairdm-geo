import re

from django.db import models
from django.utils.translation import gettext as _
from research_vocabs.models import AbstractConcept

from fairdm_geo.vocabularies import stratigraphy

# this captures age values from the comment field of GeologicalEra concepts
AGE_PATTERN = re.compile(
    r"(?P<bound_type>older|younger) bound (?P<year>-?\d+(\.\d+)?)(?: \+\|-(?P<uncertainty>\d+(\.\d+)?))? Ma"
)


class GeologicalTimescale(AbstractConcept):
    vocabulary_name = None
    _vocabulary = stratigraphy.GeologicalTimescale()
    vocabulary = None
    name = models.CharField(_("name"), max_length=255, unique=True, primary_key=True)
    older_bound = models.FloatField(_("older bound"), blank=True, null=True)
    older_bound_uncertainty = models.FloatField(_("older bound uncertainty"), blank=True, null=True)
    younger_bound = models.FloatField(_("younger bound"), blank=True, null=True)
    younger_bound_uncertainty = models.FloatField(_("lower bound uncertainty"), blank=True, null=True)

    class Meta:
        verbose_name = _("Geological Era")
        verbose_name_plural = _("Geological Eras")

    def __str__(self):
        return f"{self.label}"

    def _age(self, value, uncertainty):
        if uncertainty:
            return f"{value} ± {uncertainty} Ma"
        return f"{value} Ma"

    def age_from(self):
        return self._age(self.older_bound, self.older_bound_uncertainty)

    def age_to(self):
        return self._age(self.younger_bound, self.younger_bound_uncertainty)

    @classmethod
    def _get_defaults(cls, concept):
        defaults = super()._get_defaults(concept)

        comments = concept.attrs.get("rdfs:comment", [])

        if not comments:
            return defaults

        if not isinstance(comments, list):
            comments = [comments]

        for c in comments:
            defaults.update(cls._parse_age_comment(c))

        return defaults

    @classmethod
    def _parse_age_comment(cls, comment):
        result = AGE_PATTERN.search(comment).groupdict()
        defaults = {}
        if result:
            defaults[f"{result['bound_type']}_bound"] = abs(float(result["year"]))
            if result["uncertainty"]:
                defaults[f"{result['bound_type']}_bound_uncertainty"] = float(result["uncertainty"])
        return defaults


# class StratigraphicBoundary(AbstractConcept):
#     vocabulary_name = None
#     _vocabulary = StratigraphicBoundary()

#     class Meta:
#         verbose_name = _("Stratigraphic Boundary")
#         verbose_name_plural = _("Stratigraphic Boundaries")
