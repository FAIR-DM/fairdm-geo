from multiprocessing.dummy.connection import families

import plotly.express as px
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from fairdm import plugins
from fairdm.layouts import ApplicationLayout


class Map(plugins.Explore, ApplicationLayout, TemplateView):
    menu_item = {
        "name": _("Map"),
        "icon": "map",
    }
    title = _("Map")
    page_title = families
    template_name = "fairdm_geo/plugins/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["map_source_list"] = {}
        df = px.data.carshare()
        fig = px.scatter_map(
            df,
            lat="centroid_lat",
            lon="centroid_lon",
            color="peak_hour",
            size="car_hours",
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=10,
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),  # Remove all outer margins
            paper_bgcolor="rgba(0,0,0,0)",  # Optional: transparent background
            plot_bgcolor="rgba(0,0,0,0)",  # Optional: transparent plot background
        )
        context["plot"] = fig.to_html(full_html=False, include_plotlyjs="cdn")
        return context

    def serialize_dataset_samples(self, dataset):
        return {}


# @plugins.project.register()
class ProjectMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # for dataset in self.base_object.datasets.all():
        # context["map_source_list"].update(self.serialize_dataset_samples(dataset))

        return context


# @plugins.dataset.register()
class DatasetMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["map_source_list"].update(self.serialize_dataset_samples(self.base_object))
        return context


# @plugins.sample.register()
class SampleMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# @plugins.contributor.register()
class SampleMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for dataset in self.base_object.datasets.all():
            context["map_source_list"].update(self.serialize_dataset_samples(dataset))
        return context
