from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView

from .froms import UserRegForm


def login(request):
    """Render Login Template"""

    if request.method == 'POST':
        messages.error(request, "Something Went wrong")

        return redirect('login')

    return render(request, "users/login.html")


def register(request):
    """Render register Template"""

    return render(request, "users/register.html")


class RegistrationView(CreateView):
    """Renders Registration page and create user model"""

    template_name = "users/register.html"
    form_class = UserRegForm

    def get_success_url(self) -> str:
        return reverse('login')

    def form_valid(self, form):
        """Customise to return succes message"""
        messages.success(self.request, "Successfully Created Your Account")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Failed To Register Please Check your inputs")
        return super().form_invalid(form)


def dashboard(request):
    """Render dashboard Template"""

    return render(request, "users/dashboard.html")
