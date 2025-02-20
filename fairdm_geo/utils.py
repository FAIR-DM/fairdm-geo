from django.conf import settings

EARTH_SAMPLES = getattr(settings, "EARTH_SAMPLES", [])

is_abstract = lambda x: x not in EARTH_SAMPLES

is_registered = lambda x: x in EARTH_SAMPLES
