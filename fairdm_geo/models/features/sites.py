from django.utils.translation import gettext as _
from fairdm.db.models import QuantityField
from research_vocabs.fields import ConceptField

from fairdm_geo.vocabularies.odm2 import (
    ElevationDatum,
    SiteType,
)

from ..samples.generic import GenericEarthSample, GenericHole
from ..samples.intervals import GeoDepthInterval


class SamplingLocation(GenericEarthSample):
    type = ConceptField(
        vocabulary=SiteType,
        default="unknown",
        # include_only=settings.get("SAMPLING_LOCATION_TYPES", None),
        verbose_name=_("type"),
        help_text=_("The type of sampling location."),
    )

    elevation_datum = ConceptField(
        vocabulary=ElevationDatum,
        default="MSL",
    )
    # elevation_method = ConceptField(
    #     vocabulary=SamplingFeatureType,
    #     default="site",
    #     editable=False,
    # )
    elevation = QuantityField(
        verbose_name=_("elevation"),
        base_units="m",
        unit_choices=["m", "ft"],
        null=True,
        blank=True,
        help_text=_("The site elevation in meters with reference to the specified elevation datum."),
    )

    class Meta:
        abstract = True
        verbose_name = _("sampling location")
        verbose_name_plural = _("sampling locations")

    # class Config:
    #     metadata = Metadata(
    #         **default_metadata,
    #         description=_(
    #             "A sampling location relates to a specific geographic point, defined by precise coordinates (typically latitude and longitude), where samples are collected for scientific analysis. It includes detailed information about the time and date when the location was accessed for sampling, as well as the accessibility conditions, such as terrain, transportation routes, required permits, or any logistical challenges associated with reaching the site. This comprehensive documentation ensures that the sampling efforts are reproducible and that the data collected can be accurately interpreted within the context of its geographical, temporal, and environmental settings."
    #         ),
    #         analagous_to=[
    #             "https://schema.org/Place",
    #             "https://schema.org/GeoCoordinates",
    #             SamplingFeatureType().get_concept("site"),
    #         ],
    #     )

    #     root_allowed = True
    #     # description_types = SamplingLocationDescriptions
    #     # date_types = SamplingLocationDates

    # __doc__ = Config.metadata.description


class Borehole(GeoDepthInterval, GenericHole, SamplingLocation):
    HOLE_MAX_LENGTH = 12262  # meters

    class Meta:
        abstract = True
        verbose_name = _("borehole")
        verbose_name_plural = _("boreholes")

    # class Config:
    #     metadata = Metadata(
    #         **default_metadata,
    #         description=_(
    #             "A borehole is a narrow, cylindrical shaft drilled into the ground, either vertically or at an angle, to access subsurface materials such as soil, rock, groundwater, or gas for exploration, extraction, or geotechnical investigation purposes. Boreholes are created using drilling equipment and can vary in depth from a few meters to several kilometers, depending on the purpose of the drilling. They are used in a range of applications, including geological and environmental studies, resource exploration (such as oil, gas, and minerals), groundwater monitoring, and engineering assessments for construction projects. Boreholes are characterized by their depth, diameter, orientation, and the specific methods and tools used for drilling and sampling."
    #         ),
    #         analagous_to=[
    #             "https://schema.org/Place",
    #             "https://schema.org/GeoCoordinates",
    #             SamplingFeatureType().get_concept("borehole"),
    #         ],
    #     )

    #     root_allowed = True
    #     # description_types = SamplingLocationDescriptions
    #     # date_types = SamplingLocationDates

    # __doc__ = Config.metadata.description
