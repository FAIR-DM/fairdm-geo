from fairdm_geo.models.features import SamplingLocation


class GenericSite(SamplingLocation):
    class Meta:
        abstract = False
        verbose_name = "Generic Site"
        verbose_name_plural = "Generic Sites"
