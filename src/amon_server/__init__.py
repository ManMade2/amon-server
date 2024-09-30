from flask import Flask
from .api.navigation import navigation_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(navigation_blueprint, url_prefix="/api/v1/navigation")
    return app
