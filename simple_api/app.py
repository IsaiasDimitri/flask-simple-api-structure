from flask import Flask
from simple_api import api


def create_app():
    """Main factory"""

    app = Flask(__name__)
    api.init_app(app)
    return app
