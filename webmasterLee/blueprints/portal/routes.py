"""
File: blueprints/portal/routes.py

Routes for the administration team. Mainly for building & maintaining 
customer relationships.
 

Formatting:
    - 3 Lines in between each function

Author: Logan Lee
"""
from flask import Blueprint, current_app, redirect, render_template, url_for

from ...models import (
    db, 
    DiscoveryMethod, Lead,
    Client, ClientNote
    Project, ProjectChecklist, ProjectChecklistItem,
)
from .forms import (CreateLead)


# Define our portal blueprint object.
portal = Blueprint("portal", __name__, template_folder="portal_templates")


"""
Homepage to contain general information. One thing that I want to see
is the schedule, contact requests, and project deadlines.
"""
@portal.route("/")
def home():
    elements = {"title": "Portal Home"}
    return render_template("home.html", elements=elements)



"""
General overview of current leads. 
"""
@portal.route("/leads", methods=["GET", "POST"])
def leads():
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
            flash(f"Added {new.company} to leads.")
    return render_template("leads.html", elements=elements, leads=leads, form=form)



"""
View specific lead. Contains options for creating notes, updating, or deleting.
"""
@portal.route("/leads/<int:pk>")
def view_lead(pk):
    lead = db.get_or_404(Lead, pk) 
    elements = {"title": lead.company}
    return render_template("lead.html", elements=elements, lead=lead)




@portal.route("leads/<int:pk>/notes/create")
def create_lead_note(pk):
    # note that pk is passed into url_for
    return redirect(url_for("leads.notes", pk=pk))



"""
power_hour

Generate a call sheet to run through when I am wanting to create a 
larger workload. 

Each time you load this page it will display a list of random leads, and 
the scrapers might even grab some more. 
"""
@portal.route("/leads/power-hour")
def power_hour():
    elements = {"title": "Power Hour"}
    return render_template("power_hour.html", elements=elements)



"""
crm 

Landing page for managing customers, this might be best suited in 
its own blueprint to be totally honest. 

General rundown of what is going on with my clients. Upcoming meetings,
bills, and project deadlines. 

API to my email that will track recent chains we had over projects.
"""
@portal.route("/crm")
def crm():
    clients = db.session.query(Client).all()
    elements = {"title": "CRM"}
    return render_template("crm.html", elements=elements, clients=clients)



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
