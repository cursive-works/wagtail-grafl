from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailGraflAppConfig(AppConfig):
    name = 'wagtail_grafl'
    label = 'wagtail_grafl'
    verbose_name = _("Wagtail Grafl")
