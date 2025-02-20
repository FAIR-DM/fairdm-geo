from django.contrib import admin

from .models import SimpleLithology


@admin.register(SimpleLithology)
class SimpleLithologyAdmin(admin.ModelAdmin):
    list_display = ("name", "label", "uri")
    search_fields = ("name", "label")
