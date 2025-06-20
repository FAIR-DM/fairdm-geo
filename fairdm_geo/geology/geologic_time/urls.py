from dal import autocomplete
from django.urls import path

from .models import GeologicalTimescale


class GeologicalTimescaleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return GeologicalTimescale.objects.all()


urls = [
    # URL pattern for the GeologicalTimescaleAutocomplete view
    path(
        "geological-timescale-autocomplete/",
        GeologicalTimescaleAutocomplete.as_view(),
        name="geological-timescale-autocomplete",
    ),
]
