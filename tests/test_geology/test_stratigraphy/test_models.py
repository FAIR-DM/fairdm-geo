import pytest
from django.core.exceptions import ValidationError

from fairdm_geo.vocabularies import CGI_GENETIC_CATEGORY, CGI_STRATIGRAPHIC_RANK
from tests.factories import StratigraphicUnitFactory

CONCEPT_FIELDS = [
    ("rank", CGI_STRATIGRAPHIC_RANK, CGI_GENETIC_CATEGORY),
    ("genesis", CGI_GENETIC_CATEGORY, CGI_STRATIGRAPHIC_RANK),
]


@pytest.mark.django_db
@pytest.mark.parametrize(("field", "vocabulary", "other"), CONCEPT_FIELDS)
class TestStratigraphicUnitConceptFields:
    def test_saves_with_a_concept_of_its_vocabulary(
        self, concept_from, field, vocabulary, other
    ):
        concept = concept_from(vocabulary)

        unit = StratigraphicUnitFactory(**{field: concept})

        unit.refresh_from_db()
        assert getattr(unit, f"get_{field}_uri")() == concept.uri

    def test_refuses_a_concept_of_another_vocabulary(
        self, concept_from, field, vocabulary, other
    ):
        unit = StratigraphicUnitFactory.build(**{field: concept_from(other)})

        with pytest.raises(ValidationError) as exc:
            unit.clean_fields()

        assert field in exc.value.error_dict
