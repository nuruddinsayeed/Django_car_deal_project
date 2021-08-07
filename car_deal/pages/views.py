from django.shortcuts import render


def index(request):
    """Renders Home page"""

    return render(request, "pages/index.html")


def about(request):
    "Renders About page"

    return render(request, "pages/about.html")


def services(request):
    "Renders services page"

    return render(request, "pages/services.html")


def contact(request):
    "Renders contact page"

    return render(request, "pages/contact.html")
