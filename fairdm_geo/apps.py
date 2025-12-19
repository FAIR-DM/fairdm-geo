import warnings

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EarthScienceConfig(AppConfig):
    """
    Legacy single-app configuration for FairDM Geo.

    DEPRECATED: This app configuration is deprecated. Use the multi-app structure instead:
    - fairdm_geo.core (abstract base models)
    - fairdm_geo.rocks (rock sample models)
    - fairdm_geo.sites (sampling location models)

    Add these to INSTALLED_APPS:
        INSTALLED_APPS = [
            ...
            "fairdm_geo.core",
            "fairdm_geo.rocks",
            "fairdm_geo.sites",
        ]

    Or use fairdm.setup():
        fairdm.setup(addons=["fairdm_geo.core", "fairdm_geo.rocks", "fairdm_geo.sites"])
    """

    name = "fairdm_geo"
    verbose_name = _("Earth Science (Legacy)")

    def ready(self):
        """Import config module to trigger model registration."""
        warnings.warn(
            "The 'fairdm_geo' single-app configuration is deprecated. "
            "Use the multi-app structure instead: fairdm_geo.core, fairdm_geo.rocks, fairdm_geo.sites. "
            "See documentation for migration guide.",
            DeprecationWarning,
            stacklevel=2,
        )

        # Import config module to register all geoscience models
        import fairdm_geo.config  # noqa: F401
