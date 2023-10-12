from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify


main = Blueprint("main", __name__, url_prefix="/", template_folder="templates/main")


@main.route("/", methods=['GET', 'POST'])
def index():
	# form = ScheduleEstimateForm()
	return render_template("main.html", title="CheckErr") # argument for jinja variables


@main.route("/about", methods=['GET', 'POST'])
def about():
	# form = ScheduleEstimateForm()
	# if form.validate_on_submit():
	# 	flash('Scheduling successful! Please check your email for additional information.', 'success')
	# 	# work on models to make this possible
	# else:
	# 	flash('Scheduling unsuccessful. Please check required fields.', 'danger')
	# # I think reviews should go here
	return render_template("about.html", title='About')


@main.route("/services")
def services():

	return render_template("services.html")


# - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - Form Processing - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - -
