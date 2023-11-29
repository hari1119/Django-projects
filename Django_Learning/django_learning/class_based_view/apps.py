from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ClassBasedViewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'class_based_view'

    def ready(self):
        import class_based_view.signals