from flask import Blueprint, render_template


main = Blueprint("main", __name__, url_prefix="/", template_folder="templates") 


@main.route("/")
def index():
	context = {"title": "Welcome",}
	return render_template("index.html", context=context)


@main.route("/about")
def about():

	return render_template("about.html", title='About')


@main.route("/services")
def services():

	return render_template("services.html")


@main.route("/projects")
def projects():
	context = {"title": "WebmasterLee"}
	return render_template("projects.html", context=context)