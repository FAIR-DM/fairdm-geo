from django.contrib.gis import admin

from .models import Province


@admin.register(Province)
class ProvinceAdmin(admin.GeoModelAdmin):
    change_list_template = "admin/gis/change_list.html"
    list_display = ["name", "type", "group", "last_orogen", "crust_type"]
    search_fields = [
        "name",
    ]
    list_filter = [
        "type",
        "group",
        "crust_type",
        "last_orogen",
    ]
    fields = ["geom", ("name", "group"), ("type", "crust_type", "last_orogen")]
