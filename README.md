# fairdm-geo

[![Tests](https://github.com/FAIR-DM/fairdm-geo/actions/workflows/tests.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-geo/actions/workflows/tests.yml)
[![Build](https://github.com/FAIR-DM/fairdm-geo/actions/workflows/build.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-geo/actions/workflows/build.yml)
[![Publish](https://github.com/FAIR-DM/fairdm-geo/actions/workflows/publish.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-geo/actions/workflows/publish.yml)
[![Coverage](https://codecov.io/gh/FAIR-DM/fairdm-geo/branch/main/graph/badge.svg)](https://codecov.io/gh/FAIR-DM/fairdm-geo)
[![PyPI](https://img.shields.io/pypi/v/fairdm-geo)](https://pypi.org/project/fairdm-geo/)
[![Development status](https://img.shields.io/pypi/status/fairdm-geo)](https://pypi.org/project/fairdm-geo/)
[![Python](https://img.shields.io/pypi/pyversions/fairdm-geo)](https://pypi.org/project/fairdm-geo/)
[![Django](https://img.shields.io/pypi/djversions/fairdm-geo)](https://pypi.org/project/fairdm-geo/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Licence](https://img.shields.io/github/license/FAIR-DM/fairdm-geo)](https://github.com/FAIR-DM/fairdm-geo/blob/main/LICENSE)

A FairDM add-on that gives a research data portal ready-made geoscience models: rock samples,
sampling locations and boreholes, described with terms from published controlled vocabularies.

## Why

A portal for geoscience data needs the same few things every time. It needs a way to say what a
sample is, where it was taken, and how deep in a hole it came from. It also needs the terms for
that to mean the same thing across datasets: a lithology, a geological age, a type of sampling
location.

`fairdm-geo` supplies the models for those records on top of FairDM's `Sample`. The terms come from
vocabularies that others publish and maintain (ODM2, the CGI GeoSciML vocabularies and the
International Chronostratigraphic Chart), so your portal's data uses the same words as the
published sources.

## Scope & philosophy

**What it is.** A set of Django apps that add geoscience models to a FairDM portal:

- Rock sample models: rock sample, drill core, drill cuttings, thin section and rock powder.
- Sampling location models: a sampling location, and a borehole that adds hole geometry and a
  depth interval to it.
- A stratigraphic unit model, and abstract base models for building your own earth science
  samples.

The terms those models use come from published controlled vocabularies. The package ships each
vocabulary as a file and `django-controlled-vocabularies` loads it into the database, so loading
needs no network access.

**What it deliberately is not.**

- **Not a GIS package.** Spatial relationships to geographic features are out of scope. A sample's
  point location comes from FairDM's `Sample`.
- **Not a vocabulary editor.** The shipped vocabularies are published files, kept unmodified. To
  change a term, change it with its publisher.
- **Not a portal.** It adds models to a portal that you build with FairDM. It has no pages of its
  own beyond what FairDM generates for registered models.

**Tie-break principles**, when a design choice is contested:

1. **Published terms win.** A field offers the concepts of a published vocabulary and nothing else.
   The package does not invent terms.
2. **Build on FairDM's `Sample`.** A new record type is a `Sample` subtype, so it works everywhere
   FairDM already works with samples.
3. **Install only what you use.** Sampling locations, rock samples and stratigraphy are separate
   apps, and a portal lists only the ones it wants.

## Requirements

- Python 3.13
- Django 6.0
- FairDM 0.3
- A PostgreSQL database with PostGIS, which FairDM requires

## Installation

```bash
pip install fairdm-geo
```

`fairdm-geo` does not install FairDM, because your portal already depends on it and pins its own
version.

In your portal's settings, list `fairdm_geo` as an add-on and name the apps whose models you want:

```python
# settings.py
import fairdm

fairdm.setup(
    apps=[
        "fairdm_geo.sites",
        "fairdm_geo.rocks",
    ],
    addons=["fairdm_geo"],
)
```

Listing the add-on installs `fairdm_geo.core` and `fairdm_geo.geology.stratigraphy`, which the
other apps build on. Then create the tables and load the vocabularies:

```bash
python manage.py migrate
python manage.py sync_vocabularies
```

## Quick start

Create a borehole in a dataset, giving the top and bottom of the interval it covers. The depth
fills itself in:

```python
from fairdm_geo.sites.models import Borehole

borehole = Borehole.objects.create(
    dataset=dataset,
    name="BH-1",
    elevation=412,
    top=0,
    bottom=120,
)

borehole.vertical_depth  # the distance between top and bottom, in metres
```

Create a drill core. Its specimen type starts as the ODM2 `core` concept:

```python
from fairdm_geo.rocks.models import DrillCore

core = DrillCore.objects.create(dataset=dataset, name="BH-1 core 1")
core.specimen_type  # the ODM2 specimen type "core"
```

`dataset` is a FairDM `Dataset` in your portal. Every field is listed in the
[model reference](docs/reference/models.md).

## Documentation

The documentation is built with [fairdm-docs](https://github.com/FAIR-DM/fairdm-docs) and lives in
[docs/](docs/index.md):

- [Add fairdm-geo to a portal](docs/how-to/add-fairdm-geo-to-a-portal.md)
- [Load the vocabularies](docs/how-to/load-the-vocabularies.md)
- [Models](docs/reference/models.md)
- [Vocabularies](docs/reference/vocabularies.md)

To build the site locally:

```bash
uv sync --group docs
uv run --no-sync sphinx-build -E -W -b html docs docs/_build
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Licence

MIT. See [LICENSE](LICENSE). The vocabulary files the package ships carry the licences of their
publishers. See [fairdm_geo/vocabularies/README.md](fairdm_geo/vocabularies/README.md).
