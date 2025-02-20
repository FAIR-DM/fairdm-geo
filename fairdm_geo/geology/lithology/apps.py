from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LithologyConfig(AppConfig):
    name = "fairdm_geo.geology.lithology"
    label = "lithology"
    verbose_name = _("Lithology")
