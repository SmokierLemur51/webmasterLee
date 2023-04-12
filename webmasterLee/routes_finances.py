from flask import render_template, url_for, flash, redirect, request
from webmasterLee import app, db, bcrypt

# from webmasterLee.forms import __forms__
# from webmasterLee.models import __models__

from flask_login import login_user, current_user, logout_user, login_required


''' 
	PERSONAL FINANCES SECTION
		- date
		- 
'''

@app.route("/finances")
def finance_index():
	return render_template("finances/finances_index.html")