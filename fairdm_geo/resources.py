# from fairdm.contrib.import_export.resources import SampleResource
# from import_export import fields
# from import_export.widgets import ForeignKeyWidget

# # from fairdm_geo.location.models import Point


# class LocationWidget(ForeignKeyWidget):
#     def __init__(self, model=None, **kwargs):
#         super().__init__(model=model or Point, **kwargs)

#     def clean(self, value, row=None, *args, **kwargs):
#         if row.get("latitude") and row.get("longitude"):
#             return self.model.objects.get_or_create(
#                 y=row.get("latitude"),
#                 x=row.get("longitude"),
#             )[0]
#             # return self.model.objects.filter(x=row.get("latitude"), y=row.get("longitude")).first()
#         return None


# class SampleWithLocationResource(SampleResource):
#     latitude = fields.Field(column_name="latitude", attribute="location__latitude", readonly=True)
#     longitude = fields.Field(column_name="longitude", attribute="location__longitude", readonly=True)

#     location = fields.Field(column_name="location", attribute="location", widget=LocationWidget())

#     def before_import_row(self, row, **kwargs):
#         return super().before_import_row(row, **kwargs)

#     def get_import_order(self):
#         return [*super().get_import_order(), "dataset", "sample", "location"]

#     # def get_location(self, row, **kwargs):
#     #     if row["latitude"] and row["longitude"]:
#     #         row["location"] = Point.objects.get(latitude=row["latitude"], longitude=row["longitude"])
