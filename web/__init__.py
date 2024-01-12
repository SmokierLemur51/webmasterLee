from quart import Quart
from pathlib import Path
from web.blueprints.public.routes import public
from web.blueprints.director.routes import director
from .sqlite_connection import init_db

def create_app(database_file):
    app = Quart(__name__, static_url_path="/static")
    # configurations if that isnt already obvious
    app.config.update({
        "SECRET_KEY": "secret",
        "DATABASE": Path(app.root_path) / database_file,
    })
    
    init_db(app)
    
    app.register_blueprint(public, url_prefix="/") # url -> / 
    app.register_blueprint(director, url_prefix="/directors-corner/") # url -> /directors-corner/

    
    return app