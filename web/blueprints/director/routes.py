from flask import Blueprint, render_template

director = Blueprint("director", __name__, template_folder="templates")


@director.route("/")
def home():
    elements = {"home": "Directors Corner"}
    return render_template("home.html", elements=elements)


@director.route("/projects/")
def projects():
    return render_template("projects.html",
                                 elements={"home": "Directors Corner"})


@director.route("/customers/")
def customers():
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
    return render_template("customers.html", elements=elements)


@director.route("/subscriptions/")
def subscriptions():
    return render_template("subscriptions.html",
                                 elements={"home": "Directors Corner"})


@director.route("/finances/")
def finances():
    return render_template("finances.html",
                                 elemets={"home": "Directors Corner"})
