from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StratigraphyConfig(AppConfig):
    name = "fairdm_geo.geology.stratigraphy"
    label = "stratigraphy"
    verbose_name = _("Stratigraphy")
