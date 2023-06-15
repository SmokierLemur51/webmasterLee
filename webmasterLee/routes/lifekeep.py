''' 
	These routes will encompass the lifekeep section,
	which will basically just act as a calendar/email/text
	updater that will keep you informed of what you
	need to be informed of.

	Includes
		- small things such as lauren is in the office thursdays
		- birthdays
		- holiday countdowns
		- to do list & reminders for that
		- world updates links to relevant news
		- weather
		- events etc
'''

from flask import render_template, url_for, flash, redirect, request
from webmasterLee import app, db, bcrypt


@app.route("/")
def lifekeepIndex():


	return render_template("lifekeep/lifekeepIndex.html")
