from django.contrib.gis.db import models
from django.utils.translation import gettext as _


class Plate(models.Model):
    fixtures = "https://github.com/FairDM/gis_fixtures_dump/raw/main/plates.json.xz"

    id = models.PositiveSmallIntegerField(
        primary_key=True,
        help_text=_("plate ID"),
    )
    name = models.CharField(
        max_length=100,
        help_text=_("plate name"),
    )
    reference = models.CharField(max_length=100, help_text=_("reference"), null=True)

    plate = models.CharField(
        max_length=100,
        help_text=_("plate"),
    )

    subplate_id = models.IntegerField(
        help_text=_("Latitude in decimal degrees"),
    )
    subplate_code = models.CharField(
        max_length=3,
        help_text=_("Latitude in decimal degrees"),
    )
    subplate = models.CharField(
        max_length=128,
        help_text=_("Latitude in decimal degrees"),
    )

    type = models.CharField(
        max_length=64,
        help_text=_("Latitude in decimal degrees"),
    )
    crust_type = models.CharField(
        max_length=12,
        help_text=_("Latitude in decimal degrees"),
    )

    sea_name = models.CharField(max_length=100, help_text=_("Latitude in decimal degrees"), null=True)
    domain = models.CharField(max_length=100, help_text=_("Latitude in decimal degrees"), null=True)

    area = models.FloatField(help_text=_("Latitude in decimal degrees"))
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name = _("Tectonic Plate")
        verbose_name_plural = _("Tectonic Plates")
        editable = False
