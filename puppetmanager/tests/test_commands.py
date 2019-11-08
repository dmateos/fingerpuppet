import pytest
import mock
import puppetmanager.management.commands.nodeclassify as ncommand
import puppetmanager.management.commands.configbake as bakecommand
from puppetmanager.models import Node, Configuration


# NodeClassify


VALID_YAML = """---
classes: {}
environment: production
parameters: {}

"""


def test_nodeclassify_adds_argument_to_django_command_parser():
    mock_parser = mock.Mock()
    command = ncommand.Command()
    command.add_arguments(mock_parser)

    mock_parser.add_argument.assert_called_with("node_name", nargs="+", type=str)


def test_nodeclassify_exceptions_on_invalid_parameter():
    command = ncommand.Command()
    with pytest.raises(Exception):
        command.handle(None, invalid=["Test"])


def test_nodeclassify_exceptions_on_multi_parameter():
    command = ncommand.Command()
    with pytest.raises(Exception):
        command.handle(None, node_name=["Test", "Test2"])


@pytest.mark.django_db
def test_nodeclassify_command_prints_yaml_for_valid_name(capsys):
    command = ncommand.Command()
    node = Node(name="TestNode")
    node.save()

    command.handle(None, node_name=["TestNode"])
    captured = capsys.readouterr()

    assert captured.out == VALID_YAML


@pytest.mark.django_db
def test_nodeclassify_creates_new_node_on_missing_name():
    command = ncommand.Command()
    command.handle(None, node_name=["TestNode"])

    assert Node.objects.get(name="TestNode")


@pytest.mark.django_db
def test_nodeclassify_prints_yaml_on_missing_name(capsys):
    command = ncommand.Command()
    command.handle(None, node_name=["TestNode"])
    captured = capsys.readouterr()

    assert captured.out == VALID_YAML


# @pytest.mark.django_db
# def test_nodeclassify_calls_node_update():
#    with mock.patch("puppetmanager.management.commands.nodeclassify.Node") as nmock:
#        command = ncommand.Command()
#        command.handle(None, node_name=["TestNode"])
#        nmock.return_value.update.assert_called()

# ConfigBake


def test_configbake_adds_argument_to_django_command_parser():
    mock_parser = mock.Mock()
    command = bakecommand.Command()
    command.add_arguments(mock_parser)

    mock_parser.add_argument.assert_called_with("path", nargs="+", type=str)


@pytest.mark.django_db
def test_configbake_outputs_valid_recipe_files():
    m_open = mock.mock_open()
    configuration = Configuration(name="TestConfig", data="{}")
    configuration.save()

    with mock.patch("builtins.open", m_open, create=True):
        command = bakecommand.Command()
        command.handle()

        m_open.assert_called_once_with("TestConfig_init.pp", "w+")
        m_open().write.assert_called_once_with("{}")


@pytest.mark.django_db
def test_configbake_creates_correct_directory_structure():
    m_open = mock.mock_open()
    configuration = Configuration(name="TestConfig", data="{}")
    configuration.save()

    with mock.patch("builtins.open", m_open, create=True):
        with mock.patch("puppetmanager.management.commands.configbake.os") as mock_os:
            mock_os.path.exists.return_value = False

            command = bakecommand.Command()
            command.handle(None, path=["/etc/fingerpuppet"])

            mock_os.makedirs.assert_called_with(
                "/etc/fingerpuppet/TestConfig/manifests"
            )
            m_open.assert_called_once_with(
                "/etc/fingerpuppet/TestConfig/manifests/init.pp", "w+"
            )
            m_open().write.assert_called_once_with("{}")
