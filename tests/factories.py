"""Factories for the concrete models of fairdm_geo."""

import factory
from fairdm.factories import SampleFactory

from fairdm_geo.geology.stratigraphy.models import StratigraphicUnit
from fairdm_geo.rocks.models import (
    DrillCore,
    DrillCuttings,
    RockPowder,
    RockSample,
    ThinSection,
)
from fairdm_geo.sites.models import Borehole, SamplingLocation


class SamplingLocationFactory(SampleFactory):
    class Meta:
        model = SamplingLocation


class BoreholeFactory(SampleFactory):
    class Meta:
        model = Borehole

    top = 0
    bottom = factory.Faker("pyfloat", min_value=1, max_value=500)


class RockSampleFactory(SampleFactory):
    class Meta:
        model = RockSample


class DrillCoreFactory(SampleFactory):
    class Meta:
        model = DrillCore


class DrillCuttingsFactory(SampleFactory):
    class Meta:
        model = DrillCuttings


class ThinSectionFactory(SampleFactory):
    class Meta:
        model = ThinSection


class RockPowderFactory(SampleFactory):
    class Meta:
        model = RockPowder


class StratigraphicUnitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StratigraphicUnit
