"""Blueprint da minha API v1 """

from flask import Blueprint

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")


@api_bp.route("/")
def index():
    return "<p>Hello World</p>"