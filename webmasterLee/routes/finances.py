from flask import render_template, url_for, flash, redirect, request
from webmasterLee import app, db, bcrypt

# from webmasterLee.forms import __forms__
# from webmasterLee.models import __models__

from flask_login import login_user, current_user, logout_user, login_required
import utils




''' 
	PERSONAL FINANCES SECTION
		- date
		- personal
		- professional
'''

@app.route("/finances")
@app.route("/finances/home")
def finances_index():
	# this will be the main portal to track all income
	context = {
		"income": utils.income(),
		"expenses": utils.expenses(),
	}
	return render_template("finances/finances_index.html", context=context)

@app.route("/finances/invenstments")
def finances_investments():
	
	return render_template("finances/investments.html")

@app.route("/finances/expenses")
def finances_expenses():
	return render_template("finances/expenses.html")


@app.route("/finances/personal")
def finances_personal():
	return render_template("finances/personal.html")