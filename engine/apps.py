from django.apps import AppConfig


class EngineConfig(AppConfig):
    name = 'engine'

    def ready(self):
        from . import signals
