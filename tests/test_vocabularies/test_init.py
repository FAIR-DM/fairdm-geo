import socket

import pytest
from controlled_vocabularies.fields import Vocabulary
from controlled_vocabularies.management.commands.sync_vocabularies import (
    field_vocabularies,
)
from controlled_vocabularies.models import ConceptScheme
from django.core.management import call_command

from fairdm_geo import vocabularies

SHIPPED = {
    name: value
    for name, value in vars(vocabularies).items()
    if isinstance(value, Vocabulary)
}


class TestShippedVocabularies:
    @pytest.mark.parametrize("vocabulary", SHIPPED.values(), ids=SHIPPED.keys())
    def test_every_vocabulary_has_its_file_in_the_package(self, vocabulary):
        assert vocabulary.source.is_file()

    def test_every_declared_vocabulary_is_used_by_a_field(self):
        named = set(field_vocabularies())

        unused = {v.uri for v in SHIPPED.values()} - named

        assert unused == set()

    def test_every_vocabulary_a_field_names_is_declared_in_the_package(self):
        ours = {v.uri for v in SHIPPED.values()}
        named_by_fairdm_geo = {
            uri
            for uri, declarations in field_vocabularies().items()
            if any(
                str(declaration.source).startswith(str(vocabularies.FILES))
                for declaration in declarations
            )
        }

        assert named_by_fairdm_geo == ours

    def test_sync_loads_every_vocabulary_without_the_network(self, db, monkeypatch):
        def refuse(*args, **kwargs):
            raise OSError("the network is unavailable")

        monkeypatch.setattr(socket.socket, "connect", refuse)
        ConceptScheme.objects.filter(uri__in=[v.uri for v in SHIPPED.values()]).delete()

        call_command(
            "sync_vocabularies", *[v.uri for v in SHIPPED.values()], verbosity=0
        )

        loaded = set(ConceptScheme.objects.values_list("uri", flat=True))
        assert {v.uri for v in SHIPPED.values()} <= loaded
