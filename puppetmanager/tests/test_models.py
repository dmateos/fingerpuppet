import pytest
import yaml
import mock
import os
from puppetmanager.models import Node, Classification, Configuration
from puppetmanager.signals import configuration_update


# Node
def test_node_turns_into_string():
    node = Node(name="test node")
    assert str(node) == "test node"


@pytest.mark.django_db
def test_node_external_classify_format():
    expected_data = {"classes": {}, "parameters": {}, "environment": "production"}
    expected_data = yaml.dump(
        expected_data, default_flow_style=False, explicit_start=True
    )

    node = Node(name="test node")
    node.save()

    yaml_data = node.external_classify()

    assert yaml_data == expected_data


@pytest.mark.django_db
def test_node_external_classify_lists_configurations_in_classification():
    expected_data = {
        "classes": {"testconfiguration": {}, "testconfiguration2": {}},
        "parameters": {},
        "environment": "production",
    }

    expected_data = yaml.dump(
        expected_data, default_flow_style=False, explicit_start=True
    )

    configuration = Configuration(name="testconfiguration")
    configuration.save()

    configuration2 = Configuration(name="testconfiguration2")
    configuration2.save()

    classification = Classification()
    classification.save()
    classification.configurations.add(configuration)

    classification2 = Classification()
    classification2.save()
    classification2.configurations.add(configuration2)

    node = Node(name="test node")
    node.save()
    node.classifications.add(classification)
    node.classifications.add(classification2)

    yaml_data = node.external_classify()

    assert yaml_data == expected_data


@pytest.mark.django_db
def test_node_external_classify_doesnt_list_unrelated_configuration():
    expected_data = {
        "classes": {"testconfiguration": {}},
        "parameters": {},
        "environment": "production",
    }

    expected_data = yaml.dump(
        expected_data, default_flow_style=False, explicit_start=True
    )

    configuration = Configuration(name="testconfiguration")
    configuration.save()

    configuration2 = Configuration(name="testconfiguration2")
    configuration2.save()

    classification = Classification()
    classification.save()
    classification.configurations.add(configuration)

    classification2 = Classification()
    classification2.save()
    classification2.configurations.add(configuration2)

    node = Node(name="test node")
    node.save()
    node.classifications.add(classification)

    yaml_data = node.external_classify()

    assert yaml_data == expected_data


@pytest.mark.django_db
def test_node_update_increments_checkin_count():
    node = Node(name="test node")
    node.save()

    assert node.total_checkins == 0

    node.update()
    node.update()

    assert node.total_checkins == 2


# Configuration
def test_configuration_turns_into_string():
    configuration = Configuration(name="testconfiguration")
    assert str(configuration) == "testconfiguration"


def test_configuration_bake_data_to_file_writes_file():
    m_open = mock.mock_open()
    with mock.patch("builtins.open", m_open, create=True):
        with mock.patch("puppetmanager.models.os") as mock_os:
            mock_os.path.exists.return_value = False

            configuration = Configuration(name="TestConfig")
            configuration.data = "{}"

            configuration.bake_to_file("/etc/fingerpuppet")

            mock_os.makedirs.assert_called_with(
                "/etc/fingerpuppet/TestConfig/manifests"
            )
            m_open.assert_called_once_with(
                "/etc/fingerpuppet/TestConfig/manifests/init.pp", "w+"
            )
            m_open().write.assert_called_once_with("{}")


def test_configuration_signal_saves_only_when_path_set():
    pass


# Classification
def test_classification_turns_into_string():
    mock_config = mock.Mock()
    configuration_update(None, mock_config)
    assert not mock_config.bake_to_file.called

    os.environ["PUPPET_MODULE_PATH"] = "/test"
    configuration_update(None, mock_config)
    mock_config.bake_to_file.assert_called_with("/test")
