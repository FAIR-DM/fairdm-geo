# FairDM Geo - Geoscience Addon for FairDM

[![Github Build](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/build.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/build.yml)
[![Github Docs](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/docs.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-earth-science/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/FAIR-DM/fairdm-earth-science/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/FAIR-DM/fairdm-earth-science)
![GitHub](https://img.shields.io/github/license/FAIR-DM/fairdm-earth-science)
![GitHub last commit](https://img.shields.io/github/last-commit/FAIR-DM/fairdm-earth-science)

A FairDM framework addon providing ready-to-use geoscience data models and controlled vocabularies for geological research projects.

## Features

### Modular Multi-App Architecture

FairDM Geo is organized into separate Django apps for maximum flexibility:

- **`fairdm_geo.core`** - Abstract base models (GenericEarthSample, GenericHole, intervals)
- **`fairdm_geo.rocks`** - Rock sample models (RockSample, DrillCore, ThinSection, etc.)
- **`fairdm_geo.sites`** - Sampling location models (SamplingLocation, Borehole)

Install only the apps you need for your project.

### Geoscience Sample Models

Concrete sample models ready to use in your projects:

- **Rock Samples**: General rock specimens for geological analysis
- **Drill Cores**: Core samples from drilling operations with stratigraphic information
- **Drill Cuttings**: Rock fragments from drilling for continuous geological profiling
- **Thin Sections**: Microscopic rock sections for petrographic analysis
- **Rock Powder**: Prepared samples for geochemical analysis

### Sampling Features

- **Sampling Locations**: Geographic points with coordinates and elevation data
- **Boreholes**: Drilled holes with detailed geometry (azimuth, inclination, depth)

### Controlled Vocabularies

Pre-configured integration with ODM2 (Observations Data Model 2) vocabularies:
- Medium types (rock, water, soil, etc.)
- Sampling feature types (specimen, site, borehole)
- Specimen types (core, cuttings, thin section, powder)
- Site types and elevation datums

## Installation

Add fairdm-geo to your FairDM project:

```python
# In your main settings.py or config/__init__.py
import fairdm

fairdm.setup(
    apps=["your_app"],
    addons=[
        "fairdm_geo.core",   # Required - provides abstract base models
        "fairdm_geo.rocks",  # Optional - rock sample models
        "fairdm_geo.sites",  # Optional - sampling location models
    ],
)
```

All geoscience models are automatically registered and available for use.

### Selective Installation

Install only the apps you need:

```python
# Just rock samples, no sampling locations
fairdm.setup(
    apps=["your_app"],
    addons=[
        "fairdm_geo.core",
        "fairdm_geo.rocks",
    ],
)

# Just sampling locations, no rock samples  
fairdm.setup(
    apps=["your_app"],
    addons=[
        "fairdm_geo.core",
        "fairdm_geo.sites",
    ],
)
```

## Configuration

No configuration required! All models are concrete and ready to use out of the box.

The old `EARTH_SAMPLES` setting is no longer needed - models are always concrete.

## Usage

### Working with Geoscience Samples

The registered sample models integrate seamlessly with FairDM's core functionality:

```python
from fairdm_geo.rocks.models import RockSample, DrillCore
from fairdm_geo.sites.models import SamplingLocation, Borehole

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

# Create a drill core with detailed information
core = DrillCore.objects.create(
    name="Core DC-001",
    dataset=my_dataset,
    parent=borehole,
    status="available",
    specimen_type="core",
)
```

### Using Controlled Vocabularies

All models come with pre-configured ODM2 vocabulary fields:

```python
from fairdm_geo.models.samples import RockSample

# Vocabularies are available as model fields
sample = RockSample.objects.create(
    name="Sample RS-002",
    dataset=my_dataset,
    medium="rock",  # From ODM2 Medium vocabulary
    specimen_type="core",  # From ODM2 SpecimenType vocabulary
)
```

### Extending Models

You can extend the abstract base classes to create custom sample types:

```python
from fairdm_geo.models.samples import BaseRock

class CustomRockType(BaseRock):
    \"\"\"Custom rock sample with additional fields.\"\"\"
    
    custom_field = models.CharField(max_length=100)
    
    class Meta(BaseRock.Meta):
        verbose_name = "Custom Rock Sample"
```

## Model Hierarchy

```
Sample (FairDM core)
└── GenericEarthSample (fairdm_geo base)
    ├── BaseRock (abstract)
    │   ├── RockSample
    │   ├── DrillCore
    │   ├── DrillCuttings
    │   ├── ThinSection
    │   └── RockPowder
    └── SamplingLocation
        └── Borehole
```

All models inherit from FairDM's core `Sample` model, gaining standard features like:
- Dataset association
- Project hierarchies
- Metadata tracking
- Permissions system
- Auto-generated admin interfaces
- REST API endpoints (if enabled)

## Development

### Running Tests

```bash
poetry run pytest
poetry run pytest --cov  # With coverage
```

### Project Structure

```
fairdm_geo/
├── models/          # Model definitions
│   ├── samples/     # Rock samples (RockSample, DrillCore, etc.)
│   └── features/    # Sampling features (SamplingLocation, Borehole)
├── config.py        # Model registrations with FairDM
├── settings.py      # Addon configuration
└── vocabularies/    # ODM2 vocabulary integration
```

## Contributing

Contributions are welcome! This addon focuses on:
- **Core models**: Reusable, well-documented geoscience sample types
- **Vocabularies**: Integration with standard controlled vocabularies (ODM2, etc.)
- **Documentation**: Clear examples and migration guides

For visualization or analysis plugins, consider creating separate dedicated addons that depend on fairdm-geo.

## License

MIT License - see LICENSE file for details

## Links

- **Repository**: https://github.com/FAIR-DM/fairdm-geo
- **FairDM Framework**: https://github.com/FAIR-DM/fairdm
- **Documentation**: https://fairdm.org
- **ODM2 Vocabularies**: http://vocabulary.odm2.org/

