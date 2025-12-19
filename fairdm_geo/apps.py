from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EarthScienceConfig(AppConfig):
    name = "fairdm_geo"
    verbose_name = _("Earth Science")

    def ready(self):
        """Import config and plugins modules to trigger model and plugin registration."""
        # Import config module to register all geoscience models
        import fairdm_geo.config  # noqa: F401

        # Import plugins module to register all plugins
        import fairdm_geo.plugins  # noqa: F401
