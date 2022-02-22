import pytest
from config import Settings, get_current_app_settings, get_initial_app_settings


@pytest.mark.integration
def test_settings():
    assert Settings()


@pytest.mark.integration
def test_initial_settings():
    assert get_initial_app_settings()


@pytest.mark.integration
def test_current_settings():
    assert get_current_app_settings()
