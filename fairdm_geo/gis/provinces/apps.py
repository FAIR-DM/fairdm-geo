from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProvinceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fairdm_geo.gis.provinces"
    verbose_name = _("Geologic Province")
    verbose_name_plural = _("Geologic Provinces")
