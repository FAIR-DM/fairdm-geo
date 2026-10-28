import pytest
from django.apps import apps
from django.core.management import call_command
from django.db import connection
from django.db.migrations.executor import MigrationExecutor

APP_LABELS = [
    "fairdm_geo_core",
    "fairdm_geo_stratigraphy",
    "fairdm_geo_sites",
    "fairdm_geo_rocks",
]
APPS_WITH_MODELS = [
    "fairdm_geo_stratigraphy",
    "fairdm_geo_sites",
    "fairdm_geo_rocks",
]


def own_fields():
    """Return every field fairdm_geo declares itself on one of its concrete models."""
    return [
        pytest.param(field, id=f"{model._meta.label}.{field.name}")
        for label in APPS_WITH_MODELS
        for model in apps.get_app_config(label).get_models()
        for field in [*model._meta.local_fields, *model._meta.local_many_to_many]
        if not field.auto_created
    ]


class TestInstallation:
    @pytest.mark.parametrize("label", APP_LABELS)
    def test_every_app_is_installed(self, label):
        assert apps.is_installed(apps.get_app_config(label).name)

    @pytest.mark.parametrize("label", APPS_WITH_MODELS)
    def test_every_app_with_models_has_one_initial_migration(self, db, label):
        graph = MigrationExecutor(connection).loader.graph

        nodes = sorted(name for app, name in graph.nodes if app == label)

        assert nodes == ["0001_initial"]

    def test_every_migration_is_applied(self, db):
        executor = MigrationExecutor(connection)

        plan = executor.migration_plan(executor.loader.graph.leaf_nodes())

        assert plan == []

    def test_no_model_change_is_missing_a_migration(self, db):
        call_command("makemigrations", check=True, dry_run=True, verbosity=0)


@pytest.mark.parametrize("field", own_fields())
def test_every_field_has_a_verbose_name_and_help_text(field):
    assert field.help_text
    assert field._verbose_name
