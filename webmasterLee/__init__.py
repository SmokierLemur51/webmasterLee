from flask import Flask

from .config import Config
from .extensions import db, bcrypt

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="/static")

    # app.config.from_object(Config)
    # app.config["DATABASE"] = "testing.db"
    
    # create sqlite3 database
    # from . import data
    # data.init_app(app)
    with app.app_context():
        db.init_app(app)
        bcrypt.init_app(app)


    from webmasterLee.main.views import main
    app.register_blueprint(main, url_prefix="/")

    from webmasterLee.portal.views import portal
    app.register_blueprint(portal, url_prefix="/portal")

    from webmasterLee.client.views import client
    app.register_blueprint(client, url_prefix="/clients")

    return app
