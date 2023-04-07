from flask import render_template, url_for, flash, redirect, request
from webmasterLee import app, db, bcypt

# from webmasterLee.forms import __forms__
# from webmasterLee.models import __models__

from flask_login import login_user, current_user, logout_user, login_required


''' 
	*** BASIC ROUTES *** 
		- index
		- about/services
		- contact
		- setup account
		- payment
	
'''



@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html", title="Homepage")



# from webmasterLeeAdministration import __administrator__

'''
	*** ADMINISTRATIVE ROUTES ***
		- separate package or contain within?

'''