__license__ = "MIT License <http://www.opensource.org/licenses/mit-license.php>"
__authors__ = ["Sam Jennings"]
__docformat__ = "numpy"
__version__ = "0.0.1"
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace("-", ".", 1).split(".")])
__status__ = "Development"

# FairDM addon setup - points to settings module for configuration
__fdm_setup_module__ = "fairdm_geo.settings"
