from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StratigraphyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fairdm_geo.geology.stratigraphy"
    label = "fairdm_geo_stratigraphy"
    verbose_name = _("Stratigraphy")
