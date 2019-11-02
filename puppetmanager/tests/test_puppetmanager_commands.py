import pytest
import mock
from puppetmanager.management.commands.nodeclassify import Command
from puppetmanager.models import Node


# NodeClassify


VALID_YAML = """---
classes: {}
environment: production
parameters: {}

"""


def test_nodeclassify_adds_argument_to_django_command_parser():
    mock_parser = mock.Mock()
    command = Command()
    command.add_arguments(mock_parser)

    mock_parser.add_argument.assert_called_with("node_name", nargs="+", type=str)


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
def test_nodeclassify_command_prints_yaml_for_valid_name(capsys):
    command = Command()
    node = Node(name="TestNode")
    node.save()

    command.handle(None, node_name=["TestNode"])
    captured = capsys.readouterr()

    assert captured.out == VALID_YAML


@pytest.mark.django_db
def test_nodeclassify_creates_new_node_on_missing_name():
    command = Command()
    command.handle(None, node_name=["TestNode"])

    assert Node.objects.filter(name="TestNode")


@pytest.mark.django_db
def test_nodeclassify_prints_yaml_on_missing_name(capsys):
    command = Command()
    command.handle(None, node_name=["TestNode"])
    captured = capsys.readouterr()

    assert captured.out == VALID_YAML


# @pytest.mark.django_db
# def test_nodeclassify_calls_node_update():
#    with mock.patch("puppetmanager.management.commands.nodeclassify.Node") as nmock:
#        command = Command()
#        command.handle(None, node_name=["TestNode"])
#        nmock.return_value.update.assert_called()
