from django.apps import AppConfig


class PuppetmanagerConfig(AppConfig):
    name = "puppetmanager"

    def ready(self):
        from . import signals
