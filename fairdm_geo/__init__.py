__license__ = "MIT License <http://www.opensource.org/licenses/mit-license.php>"
__authors__ = ["Sam Jennings"]
__docformat__ = "numpy"
__version__ = "0.3.0"
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace("-", ".", 1).split(".")])
__status__ = "Development"

# FairDM addon setup - DEPRECATED
# Use fairdm.setup(addons=["fairdm_geo.core", "fairdm_geo.rocks", "fairdm_geo.sites"])
__fdm_setup_module__ = "fairdm_geo.settings"

# Backward compatibility imports
# These allow existing code to import models from fairdm_geo.models
# New code should import from sub-apps: fairdm_geo.rocks.models, fairdm_geo.sites.models
try:
    from fairdm_geo.rocks.models import (
        BaseRock,
        DrillCore,
        DrillCuttings,
        RockPowder,
        RockSample,
        ThinSection,
    )
    from fairdm_geo.sites.models import Borehole, SamplingLocation

    __all__ = [
        "BaseRock",
        "RockSample",
        "DrillCore",
        "DrillCuttings",
        "ThinSection",
        "RockPowder",
        "SamplingLocation",
        "Borehole",
    ]
except ImportError:
    # Apps not yet installed - this is expected during initial setup
    __all__ = []

