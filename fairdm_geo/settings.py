"""
FairDM Geo Addon Settings

This module defines the settings for the FairDM Geo addon, including:
- EARTH_SAMPLES: List of geoscience sample models to register as concrete (non-abstract)
- Geospatial configuration (CRS, coordinate precision)
- Icon aliases for geoscience-specific UI elements

These settings can be overridden in the main project's settings.py file.
"""

from django.conf import settings

# Define which earth science sample models should be registered as concrete models
# Models not in this list will remain abstract base classes
EARTH_SAMPLES = getattr(
    settings,
    "EARTH_SAMPLES",
    [
        # Rock samples
        "RockSample",
        "DrillCore",
        "DrillCuttings",
        "ThinSection",
        "RockPowder",
        # Sampling features
        "SamplingLocation",
        "Borehole",
    ],
)

# Geospatial configuration
# Default coordinate reference system (can be any format supported by pyproj.CRS.from_user_input())
CRS = getattr(settings, "EARTH_SCIENCE_CRS", 4326)

# Coordinate field precision configuration
X_COORD = getattr(
    settings,
    "EARTH_SCIENCE_X_COORD",
    {
        "decimal_places": 6,
        "max_digits": None,
    },
)

Y_COORD = getattr(
    settings,
    "EARTH_SCIENCE_Y_COORD",
    {
        "decimal_places": 6,
        "max_digits": None,
    },
)

# Icon aliases for geoscience UI elements
EASY_ICONS = globals().get("EASY_ICONS", {})
if "aliases" not in EASY_ICONS:
    EASY_ICONS["aliases"] = {}

EASY_ICONS["aliases"].update(
    {
        "location": "fas fa-map-marker-alt",
        "rock": "fas fa-mountain",
        "borehole": "fas fa-arrows-alt-v",
        "core": "fas fa-columns",
        "elevation": "fas fa-chart-line",
        "coordinates": "fas fa-crosshairs",
    }
)
