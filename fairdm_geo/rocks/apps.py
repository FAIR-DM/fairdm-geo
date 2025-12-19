"""Django app configuration for fairdm_geo.rocks."""

from django.apps import AppConfig, apps
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _


class RocksConfig(AppConfig):
    """Configuration for the rock samples app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "fairdm_geo.rocks"
    label = "fairdm_geo_rocks"
    verbose_name = _("FairDM Geo - Rock Samples")

    def ready(self):
        """Import models and config when app is ready."""
        # Check that core app is installed
        if not apps.is_installed("fairdm_geo.core"):
            msg = (
                "The 'fairdm_geo.rocks' app requires 'fairdm_geo.core' to be installed. "
                "Add 'fairdm_geo.core' to INSTALLED_APPS before 'fairdm_geo.rocks'."
            )
            raise ImproperlyConfigured(msg)

        # Import models to ensure they're registered
        from . import config, models  # noqa: F401
