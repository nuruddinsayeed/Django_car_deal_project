from django.views.generic.edit import FormView
from django.contrib import messages
from django.core.mail import send_mail

from cars.models import Car
from django.shortcuts import render
from .models import Team
from pages.forms import ContactForm


def get_teams_info():
    return Team.objects.all()


def index(request):
    """Renders Home page"""

    teams = get_teams_info()

    # get all available fiels from our ddatabase to suggest search
    available_models = Car.objects.values_list(
        'model', flat=True).distinct('model')
    available_states = Car.objects.values_list(
        'state', flat=True).distinct('state')
    available_years = Car.objects.values_list(
        'year', flat=True).order_by('year').distinct('year')
    available_body_styles = Car.objects.values_list(
        'body_style', flat=True).distinct('body_style')

    data = {
        "teams": get_teams_info(),
        "featured_cars": Car.objects.order_by(
            '-created_date').filter(is_featured=True),
        "latest_cars": Car.objects.order_by('-created_date')[:6],
        "available_models": available_models,
        "available_states": available_states,
        "available_years": available_years,
        "available_body_styles": available_body_styles,
    }

    return render(request, "pages/index.html", data)


def about(request):
    "Renders About page"
    data = {"teams": get_teams_info()}

    return render(request, "pages/about.html", data)


def services(request):
    "Renders services page"

    return render(request, "pages/services.html")


def contact(request):
    "Renders contact page"

    return render(request, "pages/contact.html")


class ContactFormView(FormView):
    """render contact form and send emails"""

    form_class = ContactForm
    template_name = "pages/contact.html"
    success_url = "/contact"

    def form_valid(self, form):
        """Customise to send email succes message"""

        # Now send Email
        # all Form Data
        admin_emails = ['nuruddinsayeed@gmail.com', ]
        name = form.cleaned_data["fullname"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]

        mail_body = f'Subject: {subject}, \n\n{message}\n\nUser Email: {email}\nUser Phone:{phone}'

        send_mail(
            'CarDeal: A new Message From '+name,
            mail_body,
            'nuruddinsayeed22@gmail.com',
            admin_emails,
            fail_silently=False,
        )

        messages.success(
            self.request, "Successfully sent your message. We will try to reply you soon")
        return super().form_valid(form)
