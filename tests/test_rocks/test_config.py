import pytest
from fairdm import registry

from fairdm_geo.rocks.models import (
    DrillCore,
    DrillCuttings,
    RockPowder,
    RockSample,
    ThinSection,
)


class TestModelConfigurations:
    @pytest.mark.parametrize(
        "model", [RockSample, DrillCore, DrillCuttings, ThinSection, RockPowder]
    )
    def test_the_model_is_registered_with_fairdm(self, model):
        configuration = registry.get_for_model(model)

        assert configuration.model is model
