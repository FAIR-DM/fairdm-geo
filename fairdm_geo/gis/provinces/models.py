from django.contrib.gis.db import models
from django.utils.translation import gettext as _


class Province(models.Model):
    fixtures = "https://github.com/FairDM/gis_fixtures_dump/raw/main/provinces.json.xz"

    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    reference = models.CharField(max_length=80, null=True)
    group = models.CharField(max_length=80, null=True)
    last_orogen = models.CharField(max_length=80, null=True)
    continent = models.CharField(max_length=80, null=True)
    conjugate_1 = models.CharField(max_length=80, null=True)
    comment = models.CharField(max_length=254, null=True)
    crust_type = models.CharField(max_length=12)
    conjugate_2 = models.CharField(max_length=64, null=True)
    area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name = _("Geologic Province")
        verbose_name_plural = _("Geologic Provinces")
