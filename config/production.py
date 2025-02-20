import fairdm
from django.utils.translation import gettext_lazy as _

fairdm.setup(apps=["example"])

LANGUAGES = [
    ("en", _("English")),
    ("de", _("German")),
]
