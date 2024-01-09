from flask import Blueprint, render_template


public = Blueprint("public", __name__, template_folder="templates")

@public.route("/")
def index():
    elements = {"home": "Logan Lee Development"}
    return render_template("index.html", elements=elements)

@public.route("/projects/")
def projects():
    elements = {"home": "Logan Lee Development"}
    return render_template("projects.html", elements=elements)

@public.route("/hosting/")
def services():
    elements = {"home": "Logan Lee Development"}
    return render_template("services.html", elements=elements)