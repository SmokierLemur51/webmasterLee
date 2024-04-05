from django.shortcuts import render

# Create your views here.
def index(request):
	context = {"title": "Welcome"}
	render(request, "public/index.html", context)