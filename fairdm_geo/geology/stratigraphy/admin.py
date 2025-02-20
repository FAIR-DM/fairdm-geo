from django.contrib import admin

from .models import StratigraphicUnit


@admin.register(StratigraphicUnit)
class StratigraphicUnitAdmin(admin.ModelAdmin):
    list_display = ("rank", "genesis")
