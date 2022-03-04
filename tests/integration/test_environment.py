import pytest

from app.config import Settings, get_initial_app_settings


@pytest.mark.integration
def test_settings():
    assert Settings()


@pytest.mark.integration
def test_initial_settings():
    assert get_initial_app_settings()


@pytest.mark.integration
def test_settings_host():
    settings = Settings()
    assert settings.host


@pytest.mark.integration
def test_settings_dsn():
    settings = Settings()
    assert settings.dsn
