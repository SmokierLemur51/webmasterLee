# from .extensions import clientele_login_manager, portal_login_manager
from .models import db
from .config import Config
from .blueprints.portal.routes import portal
from .blueprints.clientele.routes import clientele
from .blueprints.public.routes import public

from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="/static")

    # config 
    app.config.from_object(Config)

    # extensions
    db.init_app(app)
    # portal_login_manager
    # bcrypt.init_app(app)

    # blueprints
    app.register_blueprint(public, url_prefix="/")
    app.register_blueprint(clientele, url_prefix="/clientele")
    app.register_blueprint(portal, url_prefix="/portal")
    
    with app.app_context():
        db.metadata.create_all(db.engine)

    return app
