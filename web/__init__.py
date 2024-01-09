from quart import Quart
from web.blueprints.public.routes import public
from web.blueprints.director.routes import director

def create_app():
    app = Quart(__name__)

    app.register_blueprint(public, url_prefix="/")
    app.register_blueprint(director, url_prefix="/directors-corner/")

    return app
