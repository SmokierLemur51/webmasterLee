from quart import Blueprint
from quart.templating import render_template

public = Blueprint("public", __name__, template_folder="templates")

@public.route("/")
async def index():
    elements = {"home": "Logan Lee Development"}
    return await render_template("index.html", elements=elements)

@public.route("/portfolio/")
async def portfolio():
    elements = {"home": "Logan Lee Development"}
    return await render_template("portfolio.html", elements=elements)

@public.route("/hosting/")
async def services():
    elements = {"home": "Logan Lee Development"}
    return await render_template("services.html", elements=elements)