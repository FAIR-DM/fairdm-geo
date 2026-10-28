"""Settings a portal receives from listing fairdm_geo as an addon.

Installs the apps every other fairdm_geo app builds on. A portal adds the apps whose
models it wants (``fairdm_geo.sites``, ``fairdm_geo.rocks``) to its own ``apps``.
"""

INSTALLED_APPS = [
    *INSTALLED_APPS,  # type: ignore[has-type]  # noqa: F821
    "fairdm_geo.core",
    "fairdm_geo.geology.stratigraphy",
]
