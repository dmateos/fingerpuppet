from django.core.management.base import BaseCommand, CommandError
from puppetmanager.models import Configuration


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, *args, **options):
        try:
            path = options["path"][0]
        except KeyError:
            raise CommandError("path required")

        configs = Configuration.objects.all()
        for config in configs:
            config.bake_to_file(path)
