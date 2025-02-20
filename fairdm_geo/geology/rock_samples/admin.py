from django.contrib import admin

from .models import GeologicalTimescale


@admin.register(GeologicalTimescale)
class GeologicalTimescaleAdmin(admin.ModelAdmin):
    list_display = ("label", "age_from", "age_to")


# @admin.register(StratigraphicBoundary)
# class StratigraphicBoundaryAdmin(admin.ModelAdmin):
#     pass
