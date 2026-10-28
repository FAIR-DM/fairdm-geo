import pytest
from django.core.exceptions import ValidationError

from fairdm_geo.vocabularies import (
    MEDIUM_ROCK,
    ODM2_MEDIUM,
    ODM2_SAMPLING_FEATURE_TYPE,
    ODM2_SPECIMEN_TYPE,
    SAMPLING_FEATURE_SPECIMEN,
    SPECIMEN_TYPE_CORE,
    SPECIMEN_TYPE_CUTTINGS,
    SPECIMEN_TYPE_INDIVIDUAL_SAMPLE,
    SPECIMEN_TYPE_ROCK_POWDER,
    SPECIMEN_TYPE_THIN_SECTION,
)
from tests.factories import (
    DrillCoreFactory,
    DrillCuttingsFactory,
    RockPowderFactory,
    RockSampleFactory,
    ThinSectionFactory,
)

ROCK_FACTORIES = [
    RockSampleFactory,
    DrillCoreFactory,
    DrillCuttingsFactory,
    ThinSectionFactory,
    RockPowderFactory,
]
CONCEPT_FIELDS = [
    ("feature_type", ODM2_SAMPLING_FEATURE_TYPE, ODM2_MEDIUM),
    ("medium", ODM2_MEDIUM, ODM2_SPECIMEN_TYPE),
    ("specimen_type", ODM2_SPECIMEN_TYPE, ODM2_MEDIUM),
]


@pytest.mark.django_db
@pytest.mark.parametrize("factory", ROCK_FACTORIES)
@pytest.mark.parametrize(("field", "vocabulary", "other"), CONCEPT_FIELDS)
class TestRockConceptFields:
    def test_saves_with_a_concept_of_its_vocabulary(
        self, concept_from, factory, field, vocabulary, other
    ):
        concept = concept_from(vocabulary)

        rock = factory(**{field: concept})

        rock.refresh_from_db()
        assert getattr(rock, f"get_{field}_uri")() == concept.uri

    def test_refuses_a_concept_of_another_vocabulary(
        self, concept_from, factory, field, vocabulary, other
    ):
        rock = factory.build(**{field: concept_from(other)})

        with pytest.raises(ValidationError) as exc:
            rock.clean_fields(exclude=["dataset"])

        assert field in exc.value.error_dict


@pytest.mark.django_db
@pytest.mark.parametrize("factory", ROCK_FACTORIES)
class TestRockDefaults:
    def test_a_new_rock_is_a_specimen_of_rock(self, factory):
        rock = factory()

        rock.refresh_from_db()

        assert rock.get_feature_type_uri() == SAMPLING_FEATURE_SPECIMEN
        assert rock.get_medium_uri() == MEDIUM_ROCK


@pytest.mark.django_db
class TestSpecimenTypeDefaults:
    @pytest.mark.parametrize(
        ("factory", "expected"),
        [
            (RockSampleFactory, SPECIMEN_TYPE_INDIVIDUAL_SAMPLE),
            (DrillCoreFactory, SPECIMEN_TYPE_CORE),
            (DrillCuttingsFactory, SPECIMEN_TYPE_CUTTINGS),
            (ThinSectionFactory, SPECIMEN_TYPE_THIN_SECTION),
            (RockPowderFactory, SPECIMEN_TYPE_ROCK_POWDER),
        ],
    )
    def test_each_kind_of_rock_starts_with_its_own_specimen_type(
        self, factory, expected
    ):
        rock = factory()

        rock.refresh_from_db()

        assert rock.get_specimen_type_uri() == expected
