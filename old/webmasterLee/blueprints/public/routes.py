"""
File: blueprints/public/routes.py

Routes & endpoints for public, non authenticated users.

Author: Logan Lee 
"""
from flask import Blueprint, current_app, render_template

from ...models import db

public = Blueprint("public", __name__, template_folder="public_templates")

@public.route("/")
def index():
    """
    Index page, optimized for customer satisfaction. 
    """
    elements = {"home": "Logan Lee Development"}
    return render_template("index.html", elements=elements)

@public.route("/portfolio")
def portfolio():
    elements = {"home": "Logan Lee Development"}
    return render_template("portfolio.html", elements=elements)

@public.route("/hosting")
def services():
    elements = {"home": "Logan Lee Development"}
    return render_template("services.html", elements=elements)
