from quart import Blueprint, current_app, request, redirect, url_for
from quart.templating import render_template

from ...sqlite_connection import _get_db

director = Blueprint("director", __name__, template_folder="dtemplates")

@director.route("/")
async def home():
    """
    Shows general information about open projects, unpaid client bills, as well as 
    the status of live/production websites so I know what is online/offline.
    """
    return await render_template("home.html", 
                                    elements={"title": "Directors Corner"})



@director.route("/projects/")
async def projects():
    """
    Shows all currently unfinished projects, personal or client. Can see past/completed
    projects upon selecting the correct options for that.
    """
    return await render_template("projects.html",
                                 elements={"home": "Directors Corner"})



@director.route("projects/create/create-new-project/", methods=["POST"])
async def create_new_project():
    if request.method == "POST":
        id = 1 # assuming properly created
        return redirect(url_for(f"/projects/{id}/"))

    return redirect(url_for("/projects/"))



@director.route("/projects/<int:proj_id>/", methods=["POST"])
async def view_project(proj_id):
    """For showing information about the selected project"""
    return await render_template()



@director.route("/clients/")
async def clients():
    """
    This page is for viewing current clients/leads, as well as creating new clients/leads.
    It defaults to showing clients, you have to manually select an option to show leads.     
    """
    return await render_template("clients.html", 
                        elements={"title": "Directors Corner"})



@director.route("/clients/create-new-client/", methods=["POST"])
async def create_new_client():
    """Creating new clients, redirects to clients page after database insertion."""
    if request.method == "POST":
        form = await request.form
        if form["hiddenNewClient"]:
            print(form["phone"])
            return redirect(url_for("director.clients"))            
    return redirect(url_for("director.clients"))



@director.route("/clients/leads/create-new-lead/", methods=["POST"])
async def create_new_lead():
    """Create new leads, redirects you to clients after database insertion."""
    if request.method == "POST":
        form = await request.form
        if form["hiddenNewLead"]:
            print(form["phone"])
            return redirect(url_for("director.clients"))
    return redirect(url_for("director.clients"))



@director.route("/subscriptions/")
async def subscriptions():
    """Rundown of client subscriptions"""
    return await render_template("subscriptions.html",
                                 elements={"home": "Directors Corner"})



@director.route("/finances/")
async def finances():
    """
    Fincances related to lee development, general income from hourly work as well as 
    from hosting pricing or subscriptions. As well as personal and other income sources.
    Such as an API endpoint greenleaf posts things to.
    """
    return await render_template("finances.html",
                                 elemets={"home": "Directors Corner"})
