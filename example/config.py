import fairdm
from fairdm.metadata import ModelConfig

from fairdm_geo.metadata import FairDMGeoMeta

# from fairdm_geo.resources import SampleWithLocationResource
from .models import GenericSite
from .tables import GenericSiteTable


@fairdm.register(GenericSite)
class GenericSiteConfig(FairDMGeoMeta, ModelConfig):
    description = "A generic site for testing purposes."
    keywords = []
    filterset_options = {"fields": ["name", "type"]}
    # filterset_class = "example.filters.SampleFilter"
    fields = [
        ("name", "status"),
        "type",
        "location",
        "latitude",
        "longitude",
    ]
    primary_data_fields = ["type"]
    filterset_fields = ["name", "char_field"]
    # filterset_class = "example.filters.SampleFilter"
    table_class = GenericSiteTable
    # resource_class = SampleWithLocationResource
