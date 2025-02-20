from django.contrib.gis import admin

from .models import Plate


@admin.register(Plate)
class PlateAdmin(admin.GeoModelAdmin):
    change_list_template = "admin/gis/change_list.html"

    list_display = ["name", "subplate", "plate", "type", "crust_type", "domain", "area"]

    search_fields = [
        "name",
        "subplate",
    ]

    list_filter = ["plate", "type", "crust_type", "domain"]
    fields = ["geom", "id", "name", "plate", "plate_id", "poly_name", "type", "crust_type", "domain"]
