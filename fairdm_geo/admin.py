from django.apps import apps
from django.contrib import admin

from fairdm_geo.models import *
from fairdm_geo.utils import EARTH_SAMPLES


class RockSampleAdmin(admin.ModelAdmin):
    pass


# registry = {
#     RockSample: RockSampleAdmin,
#     ThinSection: RockSampleAdmin,

# }


# if "RockSample" in EARTH_SAMPLES:
#     admin.site.register(RockSample, RockSampleAdmin)

# if "ThinSection" in EARTH_SAMPLES:
#     admin.site.register(ThinSection, RockSampleAdmin)

for model in EARTH_SAMPLES:
    m = apps.get_model("fairdm_geo", model)
    admin.site.register(m, RockSampleAdmin)
