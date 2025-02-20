import fairdm
from fairdm.metadata import ModelConfig

from fairdm_geo.metadata import FairDMGeoMeta

from .models import Rock


@fairdm.register(Rock)
class RockConfig(FairDMGeoMeta, ModelConfig):
    description = "A rock sample is a naturally occurring solid material that is composed of one or more minerals or mineraloids and represents a fragment of a larger geological formation or rock unit. The sample is typically obtained from a specific location in order to study its physical properties, mineral composition, texture, structure, and formation processes."
    keywords = []
    filterset_options = {"fields": ["name", "char_field"]}
    # filterset_class = "example.filters.SampleFilter"
    fields = [
        ("name", "status"),
        "char_field",
        ("created", "modified"),
    ]
    primary_data_fields = (["char_field"],)
    description = ("A generic site for testing purposes.",)
    filterset_fields = ["name", "char_field"]
    # filterset_class = "example.filters.SampleFilter"
    table_class = "example.tables.GenericSiteTable"
