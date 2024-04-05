"""
File: blueprints/clientele/routes.py

Endpoints & logic for clientele related routes. 

There isn't really much on here except for paying your bill or checking information
about your projects. 

Author: Logan Lee
"""
from flask import Blueprint, render_template

clientele = Blueprint("clientele", __name__, template_folder="clientele_templates")

@clientele.route("/")
def welcome_page():
    """
    Greeting page to welcome back clients. Quick overview of whats going on with 
    their projects. Maybe able to put a little add for my other services. 
    """
    elements = {"title": "Welcome"}
    return render_template("welcome.html", elements=elements)


