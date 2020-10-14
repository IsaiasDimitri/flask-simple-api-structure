from .views import api_bp


def init_app(app):
    """Modifica o app, injetando o plugin da API.

    Args:
        app (Flask): App Flask que vai extender essas funcionalidades

    """
    app.register_blueprint(api_bp)