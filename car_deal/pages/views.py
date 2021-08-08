from django.shortcuts import render
from .models import Team


def get_teams_info():
    return {"teams": Team.objects.all()}


def index(request):
    """Renders Home page"""
    data = get_teams_info()

    return render(request, "pages/index.html", data)


def about(request):
    "Renders About page"
    data = get_teams_info()

    return render(request, "pages/about.html", data)


def services(request):
    "Renders services page"

    return render(request, "pages/services.html")


def contact(request):
    "Renders contact page"

    return render(request, "pages/contact.html")
