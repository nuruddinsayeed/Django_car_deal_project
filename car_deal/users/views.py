from django.shortcuts import render


def login(request):
    """Render Login Template"""

    return render(request, "users/login.html")


def register(request):
    """Render register Template"""

    return render(request, "users/register.html")


def dashboard(request):
    """Render dashboard Template"""

    return render(request, "users/dashboard.html")
