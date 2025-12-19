"""
Utility functions for FairDM Geo addon.

Provides helper functions for determining if models should be registered
as concrete or remain abstract based on the EARTH_SAMPLES configuration.
"""

from fairdm_geo import settings


def is_abstract(model_name: str) -> bool:
    """
    Check if a model should be abstract based on EARTH_SAMPLES setting.

    Args:
        model_name: Name of the model class (e.g., "RockSample")

    Returns:
        bool: True if the model should be abstract (not registered),
              False if it should be concrete (registered)
    """
    return model_name not in settings.EARTH_SAMPLES


def is_registered(model_name: str) -> bool:
    """
    Check if a model is registered in EARTH_SAMPLES setting.

    Args:
        model_name: Name of the model class (e.g., "RockSample")

    Returns:
        bool: True if the model is in EARTH_SAMPLES, False otherwise
    """
    return model_name in settings.EARTH_SAMPLES
