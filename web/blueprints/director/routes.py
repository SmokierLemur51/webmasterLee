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
def create_project_api():
    """
    This endpoint will be for json decoding of new projects created by my build_it
    project creator. 
    """
    if request.method == "POST":
        return "new project created"
    return ""


@director.route("/projects/<int:proj_id>/", methods=["POST"])
def view_project(proj_id):
    """For showing information about the selected project"""
    return render_template("project.html", elements={"title": proj_id})


@director.route("/crm/")
def crm():
    """
    Customer Relationship Management portal, for managing new leads, clients and projects. 

    Create client notes, industry knowledge, company intelligence, and leads. 
    """
    return render_template("crm.html", elements={"title": "CRM"})



@director.route("/clients/", methods=["GET", "POST"])
def clients():
    """
    This page is for viewing current clients/leads, as well as creating new clients/leads.
    It defaults to showing clients, you have to manually select an option to show leads.     
    """
    clients = db.session.query(Client).all()
    form = CreateClient()  ## ccf is the dictionary key

    if request.method == "POST" and form.validate_on_submit():
        print(form.company.data)
        return redirect(url_for("director.clients"))
    elif request.method == "POST":
        print("this is the no validate branch")

    return render_template("clients.html",
                           elements={
                               "title": "Directors Corner",
                               "clients": clients,
                           },
                           form=form,
                          )


@director.route("/clients/create-new-client/", methods=["GET","POST"])
def create_new_client():
    """Creating new clients, redirects to clients page after database insertion."""
    ccf = CreateClient()

    if ccf.validate_on_submit():
        print(ccf.company.data)
        
        return redirect(url_for("/directors-corner/clients/"))
    
    return redirect(url_for("director.clients"))


# does not currently have any links to it on the html pages
@director.route("/leads/")
def leads():
    leads = db.session.query(Lead).all()
    return render_template("leads.html",
                           elements={
                               "title": "Leads",
                               "leads": leads,
                           })


@director.route("/leads/create-new-lead/", methods=["POST"])
def create_new_lead():
    """Create new leads, redirects you to clients after database insertion."""
    clf = CreateLead()

    if clf.validate_on_submit():
        print(clf.company.data)
        return redirect(url_for("director.leads"))
        
    return redirect(url_for("director.leads"))


@director.route("/subscriptions/")
def subscriptions():
    """Rundown of client subscriptions"""
    return render_template("subscriptions.html",
                           elements={"home": "Directors Corner"})


@director.route("/finances/")
def finances():
    """
    Fincances related to lee development, general income from hourly work as well as 
    from hosting pricing or subscriptions. As well as personal and other income sources.
    Such as an API endpoint greenleaf posts things to.
    """
    return render_template("finances.html",
                           elemets={"home": "Directors Corner"})
