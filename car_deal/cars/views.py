from django.shortcuts import render


def cars(request):
    """Renders Cars Page"""

    return render(request, "cars/cars.html")
