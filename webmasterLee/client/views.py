from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify


client = Blueprint("client", __name__, url_prefix="/client", template_folder="templates/clients")


@client.route("/")
def index():

	return render_template("clients.html")


@client.route("/projects")
def projects():
	"""
	I thought this would be a good way for clients to be able to see more about
	projects I have done for them, you can also report bugs, request changes
	and other general management concepts.
	"""

	return render_template("projects.html")

# what other routes would someone need?
