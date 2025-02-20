"""Here you can define the common settings for the project. These are imported by the development and production settings files. Use this file to do things like adding extra apps, fairdm plugins, middleware, etc. to your project."""

import fairdm

fairdm.setup(
    apps=[
        "fairdm_geo",
        "fairdm_geo.geology.geologic_time",
        "fairdm_geo.geology.lithology",
        "example",
    ],
)
