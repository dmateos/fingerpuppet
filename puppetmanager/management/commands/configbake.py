import os
from django.core.management.base import BaseCommand
from puppetmanager.models import Configuration


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, *args, **options):
        configs = Configuration.objects.all()
        try:
            path = str(options["path"][0])
            if not os.path.exists(path):
                os.makedirs(path)

            for config in configs:
                config.bake_to_file(
                    "{}/{}_{}.{}".format(path, config.name, "init", "pp")
                )
        except KeyError:
            for config in configs:
                config.bake_to_file("{}_{}.{}".format(config.name, "init", "pp"))
