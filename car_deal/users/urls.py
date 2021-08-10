from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("login/", views.login, name='login'),
    path("register/", views.RegistrationView.as_view(), name='register'),
]
