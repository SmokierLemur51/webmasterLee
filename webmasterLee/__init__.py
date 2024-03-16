# from .extensions import clientele_login_manager, portal_login_manager
from .models import db
from .config import Config
from .blueprints.portal import portal
from .blueprints.clients import clients
from .blueprints.public import public

from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="/static")

    # config 
    app.config.from_object(Config)

    # extensions
    db.init_app()
    # clientele_login_manager
    # portal_login_manager

    # blueprints
    app.register_blueprint(public, url_prefix="/")
    app.register_blueprint(clients, url_prefix="/clientele")
    app.register_blueprint(portal, url_prefix="/portal")

    return app
