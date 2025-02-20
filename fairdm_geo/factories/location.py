import factory
from fairdm.factories import SampleFactory
from fairdm.factories.generic import RandomM2M

from fairdm_geo.geology.geologic_time.models import GeologicalTimescale
from fairdm_geo.geology.lithology.models import SimpleLithology
from fairdm_geo.geology.stratigraphy.models import StratigraphicUnit
from fairdm_geo.models.features.sites import Borehole

# class PointFactory(DjangoModelFactory):
#     x = factory.Faker("pyfloat", min_value=-180, max_value=180)
#     y = factory.Faker("pyfloat", min_value=-90, max_value=90)

#     samples = factory.RelatedFactoryList(
#         "fairdm.factories.SampleFactory",
#         factory_related_name="Point",
#         size=randint(2, 8),
#     )

#     class Meta:
#         model = "location.Point"


class SamplingLocationFactory(SampleFactory):
    type = factory.Faker("word")
    location = factory.SubFactory(PointFactory, samples=None)
    elevation = factory.Faker("pyfloat", min_value=-8000, max_value=3500)

    # class Meta:
    # model = "example.GenericSite"


class HoleFactory(SampleFactory):
    azimuth = factory.Faker("pyfloat", min_value=0, max_value=360)
    inclination = factory.Faker("pyfloat", min_value=0, max_value=90)
    length = factory.Faker("pyfloat", min_value=0, max_value=1000)


class VerticalIntervalFactory(SampleFactory):
    top = factory.Faker("pyfloat", min_value=0, max_value=1000)
    bottom = factory.Faker("pyfloat", min_value=0, max_value=1000)


class GeoDepthIntervalFactory(VerticalIntervalFactory):
    class Params:
        max_depth = Borehole.HOLE_MAX_LENGTH

    top = 0
    bottom = factory.Faker("pyfloat", min_value=0, max_value=1000)

    lithology = RandomM2M(SimpleLithology, related_field="lithology", count=3)
    age = RandomM2M(GeologicalTimescale, related_field="age", count=3)
    stratigraphy = RandomM2M(StratigraphicUnit, related_field="stratigraphy", count=3)


class BoreholeFactory(HoleFactory, GeoDepthIntervalFactory, SamplingLocationFactory):
    pass
