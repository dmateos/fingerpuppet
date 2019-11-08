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
def test_classification_view_create_classification(client):
    response = client.post(
        reverse("classification_create"), {"name": "ClassTest1"}, follow=True
    )
    assert response.status_code == 200
    assert "ClassTest1" in str(response.content)


@pytest.mark.django_db
def test_classification_view_update_classification(client):
    classification = Classification(name="ClassTest1")
    classification.save()

    response = client.post(
        reverse("classification_update", kwargs={"pk": classification.id}),
        {"name": "ClassTest1Update"},
        follow=True,
    )

    assert response.status_code == 200
    assert "ClassTest1Update" in str(response.content)


def test_classification_view_delete_classification(client):
    assert False


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


@pytest.mark.django_db
def test_configuration_view_create_configuration(client):
    response = client.post(
        reverse("configuration_create"),
        {"name": "ConfigTest1", "data": "{}"},
        follow=True,
    )

    assert response.status_code == 200
    assert "ConfigTest1" in str(response.content)


@pytest.mark.django_db
def test_configuration_view_update_configuration(client):
    configuration = Configuration(name="ConfigTest1")
    configuration.save()

    response = client.post(
        reverse("configuration_update", kwargs={"pk": configuration.id}),
        {"name": "ConfigTest1Update"},
        follow=True,
    )

    assert response.status_code == 200
    assert "ConfigTest1Update" in str(response.content)


@pytest.mark.django_db
def test_configuration_view_delete_configuration(client):
    assert False
