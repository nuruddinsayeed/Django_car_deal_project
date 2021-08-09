from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarsView.as_view(), name='cars'),
    path('<int:pk>/', views.CarDetailView.as_view(), name='car'),
    path('search/', views.CarSearchResult.as_view(), name='search'),
]
