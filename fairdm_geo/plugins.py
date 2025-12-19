"""
FairDM Geo Plugins

This module registers geoscience-specific plugins for the FairDM framework.
Currently provides interactive map visualization for Projects and Datasets.
"""

import plotly.express as px
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from fairdm import plugins
from fairdm.core.dataset.models import Dataset
from fairdm.core.project.models import Project


@plugins.register(Project, Dataset)
class Map(plugins.FairDMPlugin, TemplateView):
    """
    Interactive map visualization plugin for displaying sample locations.

    This plugin creates a Plotly map showing the geographic distribution of samples
    associated with a Project or Dataset. Samples with location data (latitude/longitude)
    are plotted on an interactive map with details available on hover.
    """

    title = _("Map")
    menu_item = plugins.PluginMenuItem(
        name=_("Map"),
        category=plugins.EXPLORE,
        icon="map",
    )
    template_name = "fairdm_geo/plugins/map.html"

    def get_context_data(self, **kwargs):
        """
        Build context with map visualization data.

        Returns:
            dict: Context dictionary with 'plot' containing the Plotly map HTML
        """
        context = super().get_context_data(**kwargs)

        # Get all samples with location data from the current object
        samples = self._get_samples_with_locations()

        if samples:
            # Create interactive map using Plotly
            context["plot"] = self._create_map(samples)
            context["sample_count"] = len(samples)
        else:
            context["plot"] = None
            context["sample_count"] = 0

        return context

    def _get_samples_with_locations(self):
        """
        Retrieve all samples with geographic location data.

        For Projects: Gets samples from all datasets
        For Datasets: Gets samples from the dataset

        Returns:
            QuerySet: Samples with non-null latitude and longitude
        """
        obj = self.base_object

        if isinstance(obj, Project):
            # Get samples from all datasets in the project
            samples = []
            for dataset in obj.datasets.all():
                samples.extend(
                    dataset.samples.filter(
                        latitude__isnull=False,
                        longitude__isnull=False
                    ).select_related("dataset")
                )
            return samples
        elif isinstance(obj, Dataset):
            # Get samples directly from the dataset
            return obj.samples.filter(
                latitude__isnull=False,
                longitude__isnull=False
            )

        return []

    def _create_map(self, samples):
        """
        Create an interactive Plotly map from sample location data.

        Args:
            samples: List or QuerySet of samples with location data

        Returns:
            str: HTML representation of the Plotly map
        """
        # Prepare data for plotting
        data = {
            "name": [],
            "latitude": [],
            "longitude": [],
            "dataset": [],
            "status": [],
        }

        for sample in samples:
            data["name"].append(str(sample.name))
            data["latitude"].append(float(sample.latitude))
            data["longitude"].append(float(sample.longitude))
            data["dataset"].append(str(sample.dataset.name) if sample.dataset else "Unknown")
            data["status"].append(str(sample.status) if hasattr(sample, "status") else "Unknown")

        # Create scatter map
        fig = px.scatter_map(
            data,
            lat="latitude",
            lon="longitude",
            hover_name="name",
            hover_data={"dataset": True, "status": True, "latitude": True, "longitude": True},
            zoom=3,
            height=600,
        )

        # Update layout for better integration with FairDM UI
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        return fig.to_html(full_html=False, include_plotlyjs="cdn")

