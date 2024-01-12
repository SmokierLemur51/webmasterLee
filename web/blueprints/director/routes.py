from quart import Blueprint, request, url_for
from quart.templating import render_template

director = Blueprint("director", __name__, template_folder="dtemplates")


@director.route("/")
async def home():
    return await render_template("home.html", 
                                    elements={"title": "Directors Corner"})


@director.route("/projects/")
async def projects():
    if request.method == "POST":
        print("Post")

    return await render_template("projects.html",
                                 elements={"home": "Directors Corner"})

@director.route("/projects/<int:proj_id>/", methods=["POST"])
async def view_project(proj_id):
    
    return await render_template()

@director.route("/clients/", methods=["GET", "POST"])
async def clients():
    if request.method == "POST":
        form = await request.form
        if form["newClientForm"]:
            print(form["fname"])
        elif form["newLeadForm"]:
            print(form["phone"])
        else:
            pass 

    return await render_template("clients.html", 
                        elements={"title": "Directors Corner"})


@director.route("/subscriptions/")
async def subscriptions():
    return await render_template("subscriptions.html",
                                 elements={"home": "Directors Corner"})


@director.route("/finances/")
async def finances():
    return await render_template("finances.html",
                                 elemets={"home": "Directors Corner"})
