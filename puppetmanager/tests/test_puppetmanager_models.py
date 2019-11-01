import pytest
import yaml
import mock
from puppetmanager.models import Node, Classification, Configuration


# Node
@pytest.mark.django_db
def test_external_classifier_format():
    expected_data = {"classes": {}, "parameters": {}, "environment": "production"}
    expected_data = yaml.dump(
        expected_data, default_flow_style=False, explicit_start=True
    )

    node = Node(name="test node")
    node.save()

    yaml_data = node.external_classify()

    assert yaml_data == expected_data


@pytest.mark.django_db
def test_external_classifier_lists_configurations_in_classification():
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

    classification = Classification()
    classification.save()
    classification.configurations.add(configuration)

    node = Node(name="test node")
    node.save()
    node.classifications.add(classification)

    yaml_data = node.external_classify()

    assert yaml_data == expected_data


# Configuration
def test_configuration_bakes_data_to_file():
    m = mock.mock_open()
    with mock.patch("builtins.open", m, create=True):
        configuration = Configuration(name="testconfiguration")
        configuration.data = "test data"

        configuration.bake_to_file("/test-path")

        m.assert_called_once_with("/test-path", "w+")
        m().write.assert_called_once_with("test data")
