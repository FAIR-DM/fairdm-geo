import pytest
from django.core.exceptions import ValidationError

from fairdm_geo.vocabularies import (
    ODM2_MEDIUM,
    ODM2_SITE_TYPE,
    SITE_TYPE_UNKNOWN,
)
from tests.factories import BoreholeFactory, SamplingLocationFactory

CONCEPT_FIELDS = [
    ("type", ODM2_SITE_TYPE, ODM2_MEDIUM),
]


@pytest.mark.django_db
@pytest.mark.parametrize("factory", [SamplingLocationFactory, BoreholeFactory])
@pytest.mark.parametrize(("field", "vocabulary", "other"), CONCEPT_FIELDS)
class TestSiteConceptFields:
    def test_saves_with_a_concept_of_its_vocabulary(
        self, concept_from, factory, field, vocabulary, other
    ):
        concept = concept_from(vocabulary)

        site = factory(**{field: concept})

        site.refresh_from_db()
        assert getattr(site, f"get_{field}_uri")() == concept.uri

    def test_refuses_a_concept_of_another_vocabulary(
        self, concept_from, factory, field, vocabulary, other
    ):
        site = factory.build(**{field: concept_from(other)})

        with pytest.raises(ValidationError) as exc:
            site.clean_fields(exclude=["dataset"])

        assert field in exc.value.error_dict


@pytest.mark.django_db
class TestSamplingLocation:
    def test_starts_with_an_unknown_type(self):
        site = SamplingLocationFactory()

        site.refresh_from_db()

        assert site.get_type_uri() == SITE_TYPE_UNKNOWN
