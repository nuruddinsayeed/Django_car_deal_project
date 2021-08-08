from cars.models import Car
from django.shortcuts import render
from .models import Team


def get_teams_info():
    return Team.objects.all()


def index(request):
    """Renders Home page"""

    teams = get_teams_info()
    data = {
        "teams": get_teams_info(),
        "featured_cars": Car.objects.order_by(
            '-created_date').filter(is_featured=True),
        "latest_cars": Car.objects.order_by('-created_date')[:6]
    }

    return render(request, "pages/index.html", data)


def about(request):
    "Renders About page"
    data = {"teams": get_teams_info()}

    return render(request, "pages/about.html", data)


def services(request):
    "Renders services page"

    return render(request, "pages/services.html")


def contact(request):
    "Renders contact page"

    return render(request, "pages/contact.html")
