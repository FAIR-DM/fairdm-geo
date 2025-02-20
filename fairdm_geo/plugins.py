from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from fairdm import plugins


class Map(TemplateView):
    name = _("Map")
    icon = "map"
    template_name = "fairdm_geo/plugins/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["map_source_list"] = {}
        return context

    def serialize_dataset_samples(self, dataset):
        return {}


@plugins.register(["project", "contributor"])
class ProjectMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for dataset in self.base_object.datasets.all():
            context["map_source_list"].update(self.serialize_dataset_samples(dataset))
        return context


@plugins.register(["dataset"])
class DatasetMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["map_source_list"].update(self.serialize_dataset_samples(self.base_object))
        return context


@plugins.register(["sample"])
class SampleMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
