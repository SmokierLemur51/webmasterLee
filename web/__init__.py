from quart import Quart

from quart_sqlalchemy import SQLAlchemyConfig
from quart_sqlalchemy.framework import QuartSQLAlchemy

def create_app():
    app = Quart(__name__)

    from web.public.routes import public
    app.register_blueprint(public, url_prefix="/")

    from web.director.routes import director
    app.register_blueprint(director, url_prefix="/directors-corner/")

    return app


    