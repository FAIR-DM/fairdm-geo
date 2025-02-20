from .models import GeologicalTimescale

GeologicalTimescale.preload()

#!/usr/bin/env python

"""
test_django-research-vocabs
------------

Tests for `django-research-vocabs` models module.
"""

import re

import pytest
from django.test import TestCase

from ..models import GeologicalTimescale


class GeologicalTimeScaleModelTest(TestCase):
    def setUp(self):
        self.model = GeologicalTimescale
        self.scheme = GeologicalTimescale._vocabulary

    def test_lithology_creation(self):
        concept = self.scheme.concepts()[0]
        lithology = self.model(concept=concept)
        self.assertEqual(lithology.name, concept.name)
        self.assertEqual(lithology.uri, concept.URI)
        self.assertEqual(lithology.label, concept.label())

    def test_preload(self):
        GeologicalTimescale.preload()
        self.assertEqual(GeologicalTimescale.objects.count(), len(self.scheme.choices))
        for obj in GeologicalTimescale.objects.all():
            self.assertIn(obj.name, self.scheme.values)


def parse_bound(input_str):
    # Regular expression to match the bound type, year, and optionally the uncertainty
    pattern = r"(older|younger) bound (-?\d+(\.\d+)?)(?: \+\|-(\d+(\.\d+)?))? Ma"

    # Using regex to find the values
    match = re.search(pattern, input_str)

    if match:
        bound_type = match.group(1)
        year = abs(float(match.group(2)))
        uncertainty = float(match.group(4)) if match.group(4) else None
        return {"bound_type": bound_type.capitalize(), "year": year, "uncertainty": uncertainty}
    else:
        return None


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("older bound -440.8 +|-1.2 Ma", {"bound_type": "Older", "year": 440.8, "uncertainty": 1.2}),
        ("younger bound -440 +|-1 Ma", {"bound_type": "Younger", "year": 440.0, "uncertainty": 1.0}),
        ("older bound -440 Ma", {"bound_type": "Older", "year": 440.0, "uncertainty": None}),
        ("younger bound 1234 +|-0.5 Ma", {"bound_type": "Younger", "year": 1234.0, "uncertainty": 0.5}),
        ("older bound -10.5 +|-0 Ma", {"bound_type": "Older", "year": 10.5, "uncertainty": 0.0}),
        ("younger bound 0 +|-1 Ma", {"bound_type": "Younger", "year": 0.0, "uncertainty": 1.0}),
        ("older bound 1000 Ma", {"bound_type": "Older", "year": 1000.0, "uncertainty": None}),
        ("unknown bound -100 Ma", None),  # This should not match the pattern
    ],
)
def test_parse_bound(input_str, expected):
    result = parse_bound(input_str)
    assert result == expected
