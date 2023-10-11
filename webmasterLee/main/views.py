from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from webmasterLee.forms import RegisterForm, ScheduleEstimateForm
from webmasterLee.models import ScheduleEstimate

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/", methods=['GET', 'POST'])
def home():
	form = ScheduleEstimateForm()
	return render_template("main/home.html", form=form) # argument for jinja variables


@main.route("/about", methods=['GET', 'POST'])
def about():
	form = ScheduleEstimateForm()
	if form.validate_on_submit():
		flash('Scheduling successful! Please check your email for additional information.', 'success')
		# work on models to make this possible
	else:
		flash('Scheduling unsuccessful. Please check required fields.', 'danger')
	# I think reviews should go here
	return render_template("main/about.html", title='About', form=form)




# - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - Form Processing - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - -
