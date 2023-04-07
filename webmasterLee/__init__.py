from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = ""

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# login manager ... 

from webmasterLee import routes