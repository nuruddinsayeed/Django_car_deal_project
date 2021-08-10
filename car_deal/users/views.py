from django.shortcuts import redirect, render
from django.contrib import messages


def login(request):
    """Render Login Template"""

    if request.method == 'POST':
        messages.error(request, "Something Went wrong")

        return redirect('login')

    return render(request, "users/login.html")


def register(request):
    """Render register Template"""

    return render(request, "users/register.html")


def dashboard(request):
    """Render dashboard Template"""

    return render(request, "users/dashboard.html")
