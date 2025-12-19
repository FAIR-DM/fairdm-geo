"""
FairDM Geo Addon Settings

This module defines the settings for the FairDM Geo addon:
- EARTH_SAMPLES: List of geoscience sample models to register as concrete (non-abstract)

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

