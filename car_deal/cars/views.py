from cars.models import Car
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Car


class CarsView(ListView):
    """Renders Cars page"""

    template_name = "cars/cars.html"
    model = Car
    paginate_by = 2
    context_object_name = 'cars'
    ordering = ['-created_date']

    def get_context_data(self, **kwargs):
        """customize context data to send search suggestions"""

        context = super().get_context_data(**kwargs)

        context['available_states'] = Car.objects.values_list(
            'state', flat=True).distinct('state')
        context['available_years'] = Car.objects.values_list(
            'year', flat=True).order_by('year').distinct('year')
        context['available_body_styles'] = Car.objects.values_list(
            'body_style', flat=True).distinct('body_style')
        context['available_transmissions'] = Car.objects.values_list(
            'transmission', flat=True).distinct('transmission')

        return context


class CarDetailView(DetailView):
    """Renders Single Car's Detail view Page"""

    template_name = "cars/car.html"
    model = Car
    context_object_name = 'car'


class CarSearchResult(ListView):
    """Renders Search result of cars"""

    template_name = "cars/search.html"
    # model = Car
    # paginate_by = 3
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        """customize context to provide search opitons"""

        context = super().get_context_data(**kwargs)

        context['available_models'] = Car.objects.values_list(
            'model', flat=True).distinct('model')
        context['available_states'] = Car.objects.values_list(
            'state', flat=True).distinct('state')
        context['available_years'] = Car.objects.values_list(
            'year', flat=True).order_by('year').distinct('year')
        context['available_conditions'] = Car.objects.values_list(
            'condition', flat=True).distinct('condition')
        context['available_transmissions'] = Car.objects.values_list(
            'transmission', flat=True).distinct('transmission')

        return context

    def get_queryset(self):
        """Overriding get queryset method"""

        cars = Car.objects.all().order_by('-created_date')

        keyword = self.request.GET.get('keyword')
        if keyword:
            cars = cars.filter(description__icontains=keyword)

        if 'model' in self.request.GET:
            model = self.request.GET.get('model')
            if model:
                cars = cars.filter(model__iexact=model)

        if 'state' in self.request.GET:
            state = self.request.GET.get('state')
            if state:
                cars = cars.filter(state__iexact=state)

        if 'year' in self.request.GET:
            year = self.request.GET.get('year')
            if year:
                cars = cars.filter(year__iexact=year)

        if 'body_style' in self.request.GET:
            body_style = self.request.GET.get('body_style')
            if body_style:
                cars = cars.filter(body_style__iexact=body_style)

        if 'min_price' in self.request.GET:
            min_price = self.request.GET.get('min_price')
            max_price = self.request.GET.get('max_price')

            if max_price:
                # here get = greater_that_or_equal lte = less_that_or_equal
                cars = cars.filter(price__gte=min_price, price__lte=max_price)

        if 'transmission' in self.request.GET:
            transmission = self.request.GET.get('transmission')

            if transmission:
                cars = cars.filter(transmission__iexact=transmission)

        if 'condition' in self.request.GET:
            condition = self.request.GET.get('condition')

            if condition:
                cars = cars.filter(condition__iexact=condition)

        return cars
