"""Sphinx settings for the package's documentation.

The site is built on fairdm-docs, which reads the project's name, version, authors and
repository from pyproject.toml and supplies the theme chosen there, the extensions and MyST
options. The pages are written by hand and the models are not imported, because importing
FairDM needs the GDAL library, which the documentation build does not have.
"""

from fairdm_docs.conf import *  # noqa: F403

# docs/agents/ configures tooling for automated contributors and is not part of the site.
exclude_patterns.append("agents")  # noqa: F405

# The package ships no static files of its own, and the logo and icon come from
# fairdm-docs.
html_static_path: list[str] = []
