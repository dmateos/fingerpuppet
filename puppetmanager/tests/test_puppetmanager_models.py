import pytest
import yaml
import mock
from puppetmanager.models import Node, Classification, Configuration


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
    m = mock.mock_open()
    with mock.patch("builtins.open", m, create=True):
        configuration = Configuration(name="testconfiguration")
        configuration.data = "test data"

        configuration.bake_to_file("/test-path")

        m.assert_called_once_with("/test-path", "w+")
        m().write.assert_called_once_with("test data")


# Classification
def test_classification_turns_into_string():
    classification = Classification(name="testclassification")
    assert str(classification) == "testclassification"
