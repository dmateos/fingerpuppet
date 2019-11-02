import pytest
from puppetmanager.management.commands.nodeclassify import Command
from puppetmanager.models import Node


# NodeClassify
@pytest.mark.django_db
def test_nodeclassify_exceptions_on_invalid_parameter():
    command = Command()
    with pytest.raises(Exception):
        command.handle(None, invalid=["Test"])


@pytest.mark.django_db
def test_nodeclassify_exceptions_on_multi_parameter():
    command = Command()
    with pytest.raises(Exception):
        command.handle(None, node_name=["Test", "Test2"])


@pytest.mark.django_db
def test_nodeclassify_command_returns_for_valid_name(capsys):
    valid_yaml = """---
classes: {}
environment: production
parameters: {}

"""

    command = Command()
    node = Node(name="TestNode")
    node.save()

    command.handle(None, node_name=["TestNode"])
    captured = capsys.readouterr()

    assert captured.out == valid_yaml


@pytest.mark.django_db
def test_nodeclassify_creates_new_node_on_missing_name():
    command = Command()
    command.handle(None, node_name=["TestNode"])

    assert Node.objects.filter(name="TestNode")
