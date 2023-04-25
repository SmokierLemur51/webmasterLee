from datetime import date

from flask import render_template, url_for, flash, redirect, request
from webmasterLee import app, db, bcrypt

# from webmasterLee.forms import __forms__
# from webmasterLee.models import __models__

from flask_login import login_user, current_user, logout_user, login_required


''' Temporary Testing Variables '''
tickets = {
	"incomplete": [
		{
			"title": "testing 1",
			"start": date.today(),
			"content": "this is the content",
		},
		{
			"title": "second test",
			"start": date.today(),
			"content": "second content pargraph"
		},
	],
	"complete": [
		{
			"title": "first completed",
			"end": date.today(),
			"content": "completed content",
		}
	],

}

''' ROUTES '''

@app.route("/tms")
@app.route("/tms/")
def tms_index():
	context = {
		"title": "Ticket Management System",
		"about": "For tracking, and maintaining what is going on in my project space.", 
	}

	return render_template("tms/tms_index.html", context=context)


@app.route("/tms/create")
def tms_create_ticket():

	return render_template("tms/tms_create.html")


@app.route("/tms/manage")
def tms_manage_ticket():


	return render_template("tms/tms_manage.html", tickets=tickets)


@app.route("/tms/progress")
def tms_view_progress():
	return render_template("tms/tms_progress.html")