from puppetmanager.models import Node


# Node
def test_external_classifier_format():
    expected_data = {"classes": {}, "parameters": {}, "environment": "production"}

    node = Node(name="test node")

    yaml_data = node.external_classify()

    assert yaml_data == expected_data
