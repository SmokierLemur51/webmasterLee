from flask import Blueprint, redirect, render_template, request, url_for

from ...models import Client, Lead, db
from .forms import CreateClient, CreateLead, CreateProject

director = Blueprint("director",
                     __name__,
                     template_folder="director_templates")


@director.route("/test/", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        print(request.form.get("compania"))
        return redirect(url_for("director.clients"))
    
    return redirect(url_for("director.clients"))


@director.route("/")
def home():
    """
    Shows general information about open projects, unpaid client bills, as well as 
    the status of live/production websites so I know what is online/offline.
    """
    return render_template("home.html", elements={"title": "Directors Corner"})


@director.route("/projects/")
def projects():
    """
    Shows all currently unfinished projects, personal or client. Can see past/completed
    projects upon selecting the correct options for that.
    """
    form = CreateProject()
    # form.lead_selection.choices = db.session.
    elements = {"title": "Projects"}
    return render_template("projects.html", elements=elements, form=form)


@director.route("projects/create/create-new-project/", methods=["POST"])
def create_new_project():
    if request.method == "POST":
        id = 1  # assuming properly created
        return redirect(url_for(f"/projects/{id}/"))

    return redirect(url_for("/projects/"))


@director.route("projects/create/create-api/", methods=["POST"])
