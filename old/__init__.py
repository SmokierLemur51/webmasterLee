from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from old.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()



def create_app(config_class=Config):
	app = Flask(__name__, static_url_path="/static")
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	
	login_manager.login_view = "login"
	login_manager.login_message_category = "info"
	
	from old.main.views import main
	app.register_blueprint(main)

	from old.client.views import client
	app.register_blueprint(client)

	from old.guru.views import guru
	app.register_blueprint(guru)

	return app



app = create_app()	

