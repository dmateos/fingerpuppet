from django.core.management.base import BaseCommand, CommandError
from puppetmanager.models import Node


class Command(BaseCommand):
    help = "Returns a puppet compadible external node classifier YAML output."

    def add_arguments(self, parser):
        parser.add_argument("node_name", nargs="+", type=str)

    def handle(self, *ags, **options):
        try:
            if len(options["node_name"]) != 1:
                raise CommandError("only one node name is accepted")
        except KeyError:
            raise CommandError("node_name required")

        node_name = options["node_name"][0]

        try:
            node = Node.objects.get(name=node_name)
        except Node.DoesNotExist:
            node = Node(name=node_name)
            node.save()
        print(node.external_classify())
