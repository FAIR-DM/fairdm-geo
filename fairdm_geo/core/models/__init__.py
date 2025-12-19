"""Core abstract models for earth science data."""

from .base import (
    GeoDepthInterval,
    GenericEarthSample,
    GenericHole,
    Interval,
    VerticalDepthInterval,
    VerticalInterval,
)

__all__ = [
    "GenericEarthSample",
    "GenericHole",
    "Interval",
    "VerticalInterval",
    "VerticalDepthInterval",
    "GeoDepthInterval",
]
