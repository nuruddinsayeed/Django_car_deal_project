from cars.models import Car
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Car


class CarsView(ListView):
    """Renders Cars page"""

    template_name = "cars/cars.html"
    model = Car
    paginate_by = 2
    context_object_name = 'cars'
    ordering = ['-created_date']


class CarDetailView(DetailView):
    """Renders Single Car's Detail view Page"""

    template_name = "cars/car.html"
    model = Car
    context_object_name = 'car'


class CarSearchResult(ListView):
    """Renders Search result of cars"""

    template_name = "cars/search.html"
    # model = Car
    paginate_by = 3
    context_object_name = 'cars'

    def get_queryset(self):
        """Overriding get queryset method"""

        cars = Car.objects.all()

        keyword = self.request.GET.get('keyword')
        if keyword:
            cars = Car.objects.order_by(
                '-created_date').filter(description__icontains=keyword)

        return cars
