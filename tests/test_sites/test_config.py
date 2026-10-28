import pytest
from fairdm import registry

from fairdm_geo.sites.models import Borehole, SamplingLocation


@pytest.mark.parametrize("model", [SamplingLocation, Borehole])
def test_the_model_is_registered_with_fairdm(model):
    configuration = registry.get_for_model(model)

    assert configuration.model is model
