from quart import Blueprint
from quart.templating import render_template

director = Blueprint("director", __name__, template_folder="templates")


@director.route("/")
async def home():
    elements = {"home": "Directors Corner"}
    return await render_template("home.html", elements=elements)


@director.route("/projects/")
async def projects():
    return await render_template("projects.html",
                                 elements={"home": "Directors Corner"})


@director.route("/customers/")
async def customers():
    elements = {
        "home": "Directors Corner",
        "customers": [
            {
                "customer": "Higganbotham Paint",
                "project": 1,
                "price": 200.00
            },
            {
                "customer": "Personal",
                "project": 2,
                "price": 0.00
            },
            {
                "customer": "Personal",
                "project": 3,
                "price": 0.00
            },
        ]
    }
    return await render_template("customers.html", elements=elements)


@director.route("/subscriptions/")
async def subscriptions():
    return await render_template("subscriptions.html",
                                 elements={"home": "Directors Corner"})


@director.route("/finances/")
async def finances():
    return await render_template("finances.html",
                                 elemets={"home": "Directors Corner"})
