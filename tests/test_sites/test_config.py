import pytest
from fairdm import registry

from fairdm_geo.sites.models import Borehole, SamplingLocation


class TestModelConfigurations:
    @pytest.mark.parametrize("model", [SamplingLocation, Borehole])
    def test_the_model_is_registered_with_fairdm(self, model):
        configuration = registry.get_for_model(model)

        assert configuration.model is model
