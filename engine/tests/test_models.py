import pytest

from engine.models import Account, AppConfiguration


# Account
def test_account_strings_to_name():
    account = Account(name="Test account")

    assert str(account) == "Test account"


# AppConfiguration
@pytest.mark.django_db
def test_appconfiguration_returns_latest_config():
    appconfig = AppConfiguration()
    appconfig.some_config_option = "test value"
    appconfig.save()

    appconfig2 = AppConfiguration()
    appconfig2.some_config_option = "test value 2"
    appconfig2.save()

    assert AppConfiguration.get("some_config_option") == "test value 2"
