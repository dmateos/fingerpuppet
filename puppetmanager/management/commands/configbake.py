from django.core.management.base import BaseCommand
from puppetmanager.models import Configuration


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        for config in Configuration.objects.all():
            config.bake_to_file("{}/{}.{}".format(config.name, "init", "pp"))
