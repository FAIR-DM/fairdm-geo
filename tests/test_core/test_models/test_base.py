import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from fairdm_geo.vocabularies import (
    CGI_SIMPLE_LITHOLOGY,
    ICS_TIMESCALE,
    ODM2_MEDIUM,
)
from tests.factories import BoreholeFactory


@pytest.mark.django_db
class TestVerticalDepthInterval:
    def test_depth_is_the_distance_between_top_and_bottom(self):
        borehole = BoreholeFactory(top=10, bottom=25)

        borehole.refresh_from_db()

        assert borehole.vertical_depth.magnitude == pytest.approx(15)

    def test_bottom_is_calculated_from_top_and_depth(self):
        borehole = BoreholeFactory(top=10, bottom=None, vertical_depth=5)

        borehole.refresh_from_db()

        assert borehole.bottom.magnitude == pytest.approx(15)

    def test_top_is_calculated_from_bottom_and_depth(self):
        borehole = BoreholeFactory(top=None, bottom=15, vertical_depth=5)

        borehole.refresh_from_db()

        assert borehole.top.magnitude == pytest.approx(10)

    def test_depth_alone_places_the_interval_at_the_surface(self):
        borehole = BoreholeFactory(top=None, bottom=None, vertical_depth=5)

        borehole.refresh_from_db()

        assert (borehole.top.magnitude, borehole.bottom.magnitude) == (0, 5)

    def test_a_bottom_above_the_top_is_refused(self):
        with pytest.raises(IntegrityError), transaction.atomic():
            BoreholeFactory(top=25, bottom=10)


@pytest.mark.django_db
class TestGenericHole:
    def test_a_length_beyond_the_deepest_hole_is_refused(self):
        borehole = BoreholeFactory(length=13_000)
        borehole.refresh_from_db()

        with pytest.raises(ValidationError) as exc:
            borehole.clean()

        assert exc.value.code == "hole_too_long"

    def test_a_length_within_the_deepest_hole_is_accepted(self):
        borehole = BoreholeFactory(length=1_000)
        borehole.refresh_from_db()

        borehole.clean()


@pytest.mark.django_db
class TestGeoDepthInterval:
    def test_lithology_accepts_a_concept_of_its_vocabulary(self, concept_from):
        borehole = BoreholeFactory()
        lithology = concept_from(CGI_SIMPLE_LITHOLOGY)

        borehole.lithology.add(lithology)

        assert borehole.get_lithology_uris() == [lithology.uri]

    def test_lithology_refuses_a_concept_of_another_vocabulary(self, concept_from):
        borehole = BoreholeFactory()

        with pytest.raises(ValidationError):
            borehole.lithology.add(concept_from(ODM2_MEDIUM))

    def test_age_accepts_a_concept_of_its_vocabulary(self, concept_from):
        borehole = BoreholeFactory()
        age = concept_from(ICS_TIMESCALE)

        borehole.age.add(age)

        assert borehole.get_age_uris() == [age.uri]

    def test_age_refuses_a_concept_of_another_vocabulary(self, concept_from):
        borehole = BoreholeFactory()

        with pytest.raises(ValidationError):
            borehole.age.add(concept_from(CGI_SIMPLE_LITHOLOGY))
