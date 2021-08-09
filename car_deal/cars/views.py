from cars.models import Car
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Car


class CarsView(ListView):
    """Renders Cars page"""

    template_name = "cars/cars.html"
    model = Car
    context_object_name = 'cars'
    ordering = ['-created_date']


class CarDetailView(DetailView):
    """Renders Single Car's Detail view Page"""

    template_name = "cars/car.html"
    model = Car
    context_object_name = 'car'
