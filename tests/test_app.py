# import pytest


def test_app_was_created(app):
    assert app.name == "simple_api.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_api_returns_200(client):
    assert client.get("/api/v1/").status_code == 200