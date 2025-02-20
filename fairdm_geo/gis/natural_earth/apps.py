from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TectonicPlateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fairdm_geo.gis.plates"
    verbose_name = _("Tectonic Plate")
    verbose_name_plural = _("Tectonic Plates")
