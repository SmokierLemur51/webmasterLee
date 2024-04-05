from django.shortcuts import render

# Create your views here.
def home(request):
	context = {"title": "Home"}
	render(request, "portal/home.html", context)

def leads(request):
	context = {"title": "Leads"}
	render(request, "portal/leads.html", context)

def clients(request):
	context = {"title": "Clients"}
	render(request, "portal/clients.html", context)

def projects(request):
	context = {"title": "Projects"}
	render(request, "portal/projects.html", context)

def finances(request):
	context = {"title": "Finances"}
	render(request, "portal/finances.html", context)