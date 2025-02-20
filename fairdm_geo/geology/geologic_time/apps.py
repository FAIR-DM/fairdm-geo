from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GeologicTimeConfig(AppConfig):
    name = "fairdm_geo.geology.geologic_time"
    label = "geologic_time"
    verbose_name = _("Geologic Time")
