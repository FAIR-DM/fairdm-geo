"""Django app configuration for fairdm_geo.geology.stratigraphy."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StratigraphyConfig(AppConfig):
    """Configuration for the stratigraphy app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "fairdm_geo.geology.stratigraphy"
    label = "fairdm_geo_stratigraphy"
    verbose_name = _("Stratigraphy")
