from flask import Flask

from web.models.models import db
from web.blueprints.public.routes import public
from web.blueprints.director.routes import director


def create_app():
    app = Flask(__name__, static_url_path="/static")

    app.config["SECRET_KEY"] = "mega_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testing.db"

    db.init_app(app)
    
    app.register_blueprint(public, url_prefix="/")
    app.register_blueprint(director, url_prefix="/directors-corner/")

    with app.app_context():
        db.create_all()

    return app
