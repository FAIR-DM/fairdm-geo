"""Pytest configuration shared by the whole suite."""

import pytest
from controlled_vocabularies.models import Record
from django.core.management import call_command


def seed_session_data():
    """Write what every test may rely on: FairDM's licences and every vocabulary."""
    call_command("seed_licenses", verbosity=0)
    # Read from the files each declaration points at, never over the network.
    call_command("sync_vocabularies", verbosity=0)


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        seed_session_data()


@pytest.fixture(autouse=True)
def _media_root_under_tmp_path(tmp_path, settings):
    # A test's files land in its own tmp_path, never in a path shared across runs and xdist workers.
    settings.MEDIA_ROOT = str(tmp_path / "media")
    settings.STATIC_ROOT = str(tmp_path / "static")


@pytest.fixture
def concept_from(db):
    """Return a function that picks a concept of a vocabulary from the database."""

    def pick(vocabulary, *, skip=()):
        """Return one concept of ``vocabulary``.

        Args:
            vocabulary: The ``Vocabulary`` to take the concept from.
            skip: URIs the concept must not have.

        Returns:
            A concept ``Record`` belonging to the vocabulary.
        """
        return (
            Record.objects.filter(type=Record.Type.CONCEPT, scheme__uri=vocabulary.uri)
            .exclude(uri__in=skip)
            .order_by("uri")
            .first()
        )

    return pick
