import pytest
from simple_api.app import create_app


@pytest.fixture(scope="module")
def app():
    """ Returns a fresh new Flask App"""
    return create_app()