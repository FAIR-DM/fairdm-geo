from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EarthScienceConfig(AppConfig):
    name = "fairdm_geo"
    verbose_name = _("Earth Science")
