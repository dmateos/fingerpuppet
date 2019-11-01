import pytest
from django.urls import reverse
from engine.models import Account


# Index
def test_index_loads(client):
    response = client.get("/")

    assert response.status_code == 200


# User Login/Register
@pytest.mark.django_db
def test_user_register_page_loads(client):
    response = client.get(reverse("user_register"))

    assert response.status_code == 200
    assert "Username" in str(response.content)
    assert "Password" in str(response.content)
    assert "Email address" in str(response.content)


@pytest.mark.django_db
def test_user_can_register(client):
    response = client.post(
        reverse("user_register"),
        {"username": "test", "password": "test", "email": "test@test.com"},
        follow=True,
    )

    assert "Login successful" in str(response.content)
    assert "Logout" in str(response.content)
    assert Account.objects.filter(name="test").first() is not None


@pytest.mark.django_db
def test_associated_account_is_created(client):
    client.post(
        reverse("user_register"),
        {"username": "test", "password": "test", "email": "test@test.com"},
        follow=True,
    )

    assert Account.objects.filter(name="test").first().user.username == "test"


@pytest.mark.django_db
def test_invalid_form_redirect_to_login(client):
    response = client.post(
        reverse("user_register"),
        {"username": "test", "password": "", "email": "test@test.com"},
        follow=True,
    )

    assert "Username" in str(response.content)
    assert "Password" in str(response.content)
