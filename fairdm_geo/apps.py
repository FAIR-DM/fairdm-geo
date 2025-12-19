"""Django app configuration for fairdm_geo package.

NOTE: This root app config is not meant to be installed directly.
Instead, install the individual apps:
- fairdm_geo.core (required - abstract base models)
- fairdm_geo.rocks (optional - rock sample models)
- fairdm_geo.sites (optional - sampling location models)
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EarthScienceConfig(AppConfig):
    """Root package app configuration (not for direct use)."""

    name = "fairdm_geo"
    verbose_name = _("Earth Science")
