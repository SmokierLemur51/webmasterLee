"""
File: blueprints/portal/routes.py

Routes for the administration team. Mainly for building & maintaining 
customer relationships.
 

Formatting:
    - 3 Lines in between each function

Author: Logan Lee
"""
from flask import Blueprint, current_app, redirect, render_template, url_for

from ...models import db, DiscoveryMethod, Lead
from .forms import CreateLead
from .leads import get_method_id

portal = Blueprint("portal", __name__, template_folder="portal_templates")

@portal.route("/")
def home():
    """
    Homepage to contain general information. One thing that I want to see
    is the schedule, contact requests, and project deadlines.
    """
    elements = {"title": "Portal Home"}
    return render_template("home.html", elements=elements)



@portal.route("/leads", methods=["GET", "POST"])
def leads():
    """
    General overview of current leads. 
    """
    # page data
    leads = db.session.query(Lead).all() # need to paginate results
    discovery_method_list = [[self.id, self.method] for self in db.session.query(DiscoveryMethod).all()] 
    elements = {"title": "Leads"}
    # create form instance
    form = CreateLead() 
    form.discovery_method.choices = [[_][0] for _ in discovery_method_list]
    # post form
    if form.validate_on_submit():
        new = Lead(
            discovery_method_id=form.discovery_method.data,
            company=form.company.data,
            phone=form.phone.data,
            email=form.email.data,
            contacted=form.contacted.data,
            converted=form.converted.data,
            comment=form.comment.data,
        )
        with current_app.app_context():
            db.session.add(new)
            db.session.commit()
            print(new.company)
    return render_template("leads.html", elements=elements, leads=leads, form=form)



@portal.route("/leads/<int:pk>")
def view_lead(pk):
    """
    View specific lead. Contains options for creating notes, updating, or deleting.
    """
    lead = db.get_or_404(Lead, pk) 
    elements = {"title": lead.company}
    return render_template("lead.html", elements=elements, lead=lead)



# This remains unused for now. 
@portal.route("/leads/create")
def create_lead():
    form = CreateLead()
    if form.validate_on_submit():
        print(crea)
        pass
    return redirect(url_for("portal.leads"))



@portal.route("/crm")
def crm():
    elements = {"title": "CRM"}
    return render_template("crm.html", elements=elements)



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



# @portal.route()
