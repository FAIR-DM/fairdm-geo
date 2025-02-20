from fairdm.metadata import Authority, Citation


class FairDMGeoMeta:
    authority = (
        Authority(
            name="FairDM Geo Development Team",
            short_name="FairDM Geo",
            website="https://github.com/FAIR-DM/fairdm-geo",
        ),
    )
    citation = Citation(
        text="FairDM Geo Development Team (2021). FairDM Geo: Geoscience based addons for the FairDM Framework. https://fairdm.org",
        doi="https://doi.org/10.5281/zenodo.123456",
    )
    repository_url = "https://github.com/FAIR-DM/fairdm-geo"
    keywords = ["earth_science"]
