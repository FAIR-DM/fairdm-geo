from fairdm_geo.sites.models import SamplingLocation


class GenericSite(SamplingLocation):
    class Meta:
        abstract = False
        verbose_name = "Generic Site"
        verbose_name_plural = "Generic Sites"
