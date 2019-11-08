from django.core.management.base import BaseCommand
from puppetmanager.models import Configuration


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, *args, **options):
        configs = Configuration.objects.all()
        for config in configs:
            config.bake_to_file(options["path"][0])
