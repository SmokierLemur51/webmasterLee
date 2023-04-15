from flask import render_template, url_for, flash, redirect, request
from webmasterLee import app, db, bcrypt

# from webmasterLee.forms import __forms__
# from webmasterLee.models import __models__

from flask_login import login_user, current_user, logout_user, login_required


@app.route("/tms")
def tms_index():
	return render_template("tms/tms_index.html")