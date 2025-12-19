"""Django app configuration for fairdm_geo.core."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    """Configuration for the core earth science models app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "fairdm_geo.core"
    label = "fairdm_geo_core"
    verbose_name = _("FairDM Geo - Core Models")

    def ready(self):
        """Import models when app is ready."""
        # Import models to ensure they're registered
        from . import models  # noqa: F401
