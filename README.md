# FairDM Geo - Geoscience Addon for FairDM

[![Github Build](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/build.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/build.yml)
[![Github Docs](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/docs.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/FAIR-DM/fairdm-earth-science/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/FAIR-DM/fairdm-earth-science)
![GitHub](https://img.shields.io/github/license/FAIR-DM/fairdm-earth-science)
![GitHub last commit](https://img.shields.io/github/last-commit/FAIR-DM/fairdm-earth-science)

A comprehensive addon for the FairDM framework providing geoscience-specific data models, vocabularies, and visualization tools.

## Features

### Geoscience Sample Models

- **Rock Samples**: General rock specimens for geological analysis
- **Drill Cores**: Core samples from drilling operations with stratigraphic information
- **Drill Cuttings**: Rock fragments from drilling for continuous geological profiling
- **Thin Sections**: Microscopic rock sections for petrographic analysis
- **Rock Powder**: Prepared samples for geochemical analysis

### Sampling Features

- **Sampling Locations**: Geographic points with coordinates and elevation data
- **Boreholes**: Drilled holes with detailed geometry (azimuth, inclination, depth)

### Controlled Vocabularies

Integration with ODM2 (Observations Data Model 2) vocabularies:
- Medium types (rock, water, soil, etc.)
- Sampling feature types (specimen, site, borehole)
- Specimen types (core, cuttings, thin section, powder)
- Site types and elevation datums

### Visualization

- **Interactive Maps**: Plotly-based map visualization of sample locations for Projects and Datasets

## Installation

Add fairdm-geo to your FairDM project:

```python
# In your main settings.py or config/__init__.py
import fairdm

fairdm.setup(
    apps=["your_app"],
    addons=["fairdm_geo"],
)
```

## Configuration

### Enabling Sample Models

Configure which geoscience models should be registered as concrete models in your `settings.py`:

```python
# settings.py

EARTH_SAMPLES = [
    # Rock samples
    "RockSample",
    "DrillCore",
    "DrillCuttings",
    "ThinSection",
    "RockPowder",
    # Sampling features
    "SamplingLocation",
    "Borehole",
]
```

Models not in this list will remain abstract base classes.

### Geospatial Settings

Configure coordinate precision and default CRS:

```python
# Default coordinate reference system (EPSG code or pyproj-compatible string)
EARTH_SCIENCE_CRS = 4326

# Coordinate field precision
EARTH_SCIENCE_X_COORD = {
    "decimal_places": 6,
    "max_digits": None,
}

EARTH_SCIENCE_Y_COORD = {
    "decimal_places": 6,
    "max_digits": None,
}
```

## Usage

### Creating Geoscience Samples

The registered sample models work like standard FairDM samples with additional geoscience-specific fields:

```python
from fairdm_geo.models.samples import RockSample, DrillCore
from fairdm_geo.models.features import SamplingLocation, Borehole

# Create a sampling location
site = SamplingLocation.objects.create(
    name="Field Site Alpha",
    dataset=my_dataset,
    latitude=45.5231,
    longitude=-122.6765,
    elevation=150.5,
    elevation_datum="MSL",
)

# Create a rock sample at that location
sample = RockSample.objects.create(
    name="Sample RS-001",
    dataset=my_dataset,
    parent=site,
    status="available",
)
```

### Using the Map Plugin

The Map plugin automatically appears in the plugin menu for Projects and Datasets that have samples with location data. It displays an interactive Plotly map showing sample locations, names, datasets, status, and coordinates.

## Model Hierarchy

```
Sample (FairDM core)
├── GenericEarthSample (fairdm_geo base)
│   ├── BaseRock
│   │   ├── RockSample
│   │   ├── DrillCore
│   │   ├── DrillCuttings
│   │   ├── ThinSection
│   │   └── RockPowder
│   └── SamplingLocation
│       └── Borehole
```

## Development

### Running Tests

```bash
poetry run pytest
poetry run pytest --cov  # With coverage
```

### Modern API Implementation

This addon uses the current FairDM API:

**✅ Modern Features:**
- `@register` decorator for model configuration
- `ModelConfiguration` with `ModelMetadata`, `Authority`, and `Citation`
- `@plugins.register(Model1, Model2)` for plugin registration
- `plugins.FairDMPlugin` base class
- `plugins.PluginMenuItem` with category system
- `__fdm_setup_module__` addon setup pattern
- Auto-discovery via `apps.py` `ready()` method

**❌ Removed Legacy Patterns:**
- Old `@plugins.project.register()` decorator syntax
- `plugins.Explore` and `ApplicationLayout` base classes
- Dict-based `menu_item` configuration
- Custom admin registration (now auto-generated)

## License

MIT License - see LICENSE file for details

## Links

- **Repository**: https://github.com/FAIR-DM/fairdm-geo
- **FairDM Framework**: https://github.com/FAIR-DM/fairdm
- **Documentation**: https://fairdm.org

