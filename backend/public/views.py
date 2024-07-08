from django.shortcuts import render

def index(request):
    context = {
            'title': 'Logan Lee Development',
    }
    return render(request, "public/index.html", context)


def about(request):
    context = {
            'title': 'Logan Lee Development',
    }
    return render(request, "public/about.html", context)


def contact(request):
    context = {
            'title': 'Logan Lee Development',
    }
    return render(request, "public/contact.html", context)


def portfolio(request):
    # projects
    context = {'title': 'Portfolio'}
    return render(request, "public/portfolio.html", context)