from fairdm_geo.tables import PointTable

from .models import GenericSite


class GenericSiteTable(PointTable):
    class Meta:
        model = GenericSite
        exclude = ["path", "has_children", "has_parent"]
        fields = [
            # "site",
            "dataset",
            "id",
            "name",
            "latitude",
            "longitude",
        ]
