import pytest
from django.urls import reverse
from puppetmanager.models import Node, Classification, Configuration


@pytest.mark.django_db
def test_node_list_view_shows_nodes(client):
    node_test = Node(name="NodeTest1")
    node_test.save()
    node_test = Node(name="NodeTest2")
    node_test.save()

    response = client.get(reverse("node_list"))

    assert response.status_code == 200
    assert "NodeTest1" in str(response.content)
    assert "NodeTest2" in str(response.content)


@pytest.mark.django_db
def test_classification_view_shows_entries(client):
    classification = Classification(name="ClassTest1")
    classification.save()
    classification = Classification(name="ClassTest2")
    classification.save()

    response = client.get(reverse("classification_list"))

    assert response.status_code == 200
    assert "ClassTest1" in str(response.content)
    assert "ClassTest2" in str(response.content)


@pytest.mark.django_db
def test_configuration_view_shows_entries(client):
    configuration = Configuration(name="ConfigTest1")
    configuration.save()
    configuration = Configuration(name="ConfigTest2")
    configuration.save()

    response = client.get(reverse("configuration_list"))

    assert response.status_code == 200
    assert "ConfigTest1" in str(response.content)
    assert "ConfigTest2" in str(response.content)
