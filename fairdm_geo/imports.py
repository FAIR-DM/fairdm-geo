# """Provides a specialized importer for samples with a location field."""

# from fairdm.core.models import Sample
# from fairdm_geo.location.models import Point


# class SampleLocationImporterMixin:
#     location_fields = {
#         "x": "x",
#         "y": "y",
#     }

#     def get_location(self, row):
#         """Extracts location data from the row and returns a Location object."""
#         location = {}
#         for key, value in self.location_fields.items():
#             location[key] = row.pop(value)

#         return Point.objects.get_or_create(
#             **location,
#         )[0]

#     def modify_row(self, row, model, options):
#         row = super().modify_row(row, model, options)
#         if issubclass(model, Sample):
#             row["location"] = self.get_location(row)
#         return row
