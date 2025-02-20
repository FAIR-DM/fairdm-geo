from appconf import AppConf
from django.conf import settings  # noqa: F401


class EarthScienceSettings(AppConf):
    CRS = 4326
    """Can be any of the formats supported by pyproj.CRS.from_user_input()"""

    X_COORD = {
        "decimal_places": 6,
        "max_digits": None,
    }
    """"""

    Y_COORD = {
        "decimal_places": 6,
        "max_digits": None,
    }
    """"""
