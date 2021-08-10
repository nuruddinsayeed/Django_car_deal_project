from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages, auth
from django.views.generic.edit import CreateView

from .froms import UserRegForm, LoginForm


def login(request):
    """Render Login Template"""

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # log in user
            user = auth.authenticate(
                username=data["username"], password=data["password"])

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect('dashboard')
            messages.error(
                request, "Login Failed, Please Enter valid Username and password")
            return redirect('login')

        messages.error(
            request, "Invalid Input")
        return render(request, "users/login.html", {"form": form})

    form = LoginForm()

    return render(request, "users/login.html", {"form": form})


def logout(request):
    """Log Out User"""
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect('login')
    return redirect('home')


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
