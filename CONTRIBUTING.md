# Contributing to fairdm-geo

Thank you for helping. This guide covers how to set up, how to run the tests and what a pull
request needs.

## Setting up

```bash
git clone https://github.com/FAIR-DM/fairdm-geo.git
cd fairdm-geo
uv sync
uv run pre-commit install
```

## Running the tests

The models are GeoDjango models, so the tests need PostgreSQL with PostGIS and the GDAL, GEOS and
PROJ libraries. Run them in the FairDM development image against a PostGIS database, as CI does.
With PostGIS listening on `localhost:5432` and a `postgres` user with the password `postgres`:

```bash
docker run --rm --network host --user root -v "$PWD:/app" -w /app \
  -e POSTGRES_HOST=localhost -e POSTGRES_PORT=5432 -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=fairdm_geo \
  -e DJANGO_SETTINGS_MODULE=tests.settings \
  ghcr.io/fair-dm/fairdm:1.0.0-dev sh -c 'uv sync --locked && pytest'
```

To run one file while you work, replace `pytest` with `pytest <path> -x`.

## Making a change

1. Branch from `main`.
2. Write a test first, and watch it fail for the right reason. See
   [docs/contributing/standards/testing.md](docs/contributing/standards/testing.md).
3. Make the change.
4. Run the checks:

   ```bash
   uv run pre-commit run --all-files
   uv run mypy
   uv run deptry .
   ```

5. Update the documentation in the same pull request if the change is visible to a developer who
   installs the package.
6. Add a line to `CHANGELOG.md` if the change is visible to a developer who installs the package.
7. Open a pull request that says what changed and why.

To build the documentation site:

```bash
uv sync --group docs
uv run --no-sync sphinx-build -E -W -b html docs docs/_build
```

## Standards

- [CONSTITUTION.md](CONSTITUTION.md): the rules every change follows.
- [CONTEXT.md](CONTEXT.md): the words this repository uses.
- [docs/contributing/standards/](docs/contributing/standards/): Django code, testing,
  documentation and docstrings.

## Licence

By contributing you agree that your contribution is licensed under the MIT Licence.
