import pytest
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured


def test_the_app_refuses_to_load_without_the_core_app(monkeypatch):
    monkeypatch.setattr(apps, "is_installed", lambda name: False)

    with pytest.raises(ImproperlyConfigured):
        apps.get_app_config("fairdm_geo_sites").ready()
