"""
File: blueprints/portal/routes.py

Routes for the administration team. Mainly for maintaining
cutstomer information and tracking projects. 

Author: Logan Lee
"""
from flask import Blueprint, redirect, render_template, url_for

from ...models import db, Lead
from .forms import CreateLead

portal = Blueprint("portal", __name__, template_folder="portal_templates")

@portal.route("/home")
def homepage():
    """
    """
    elements = {"title": "Portal Home"}
    return render_template("home.html", elements=elements)

@portal.route("/leads")
def leads():
    """
    General overview of current leads. 
    """
    leads = db.session.query(Lead).all() # eventually want to filter by good leads
    elements = {
        "title": "Leads",

    }
    create_form = CreateLead()
    return render_template("leads.html", elements=elements, leads=leads)


@portal.route("/projects")
def projects():
    elements = {"title": "Projects"}
    return render_template("projects.html", elements=elements)


@portal.route("/projects/<int:project_id>")
def show_project(project_id):
    elements = {"title": "Project {}".format()}
    return render_template("project.html", elements=elements)


@portal.route("/projects/<int:project_id>/update", methods=["POST"])
def update_project(project_id):
    # update project here
    return redirect(url_for("show_project"))
