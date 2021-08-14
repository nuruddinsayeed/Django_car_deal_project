from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail

from cars.models import Car
from users.models import CustomUser
from inquiry.models import Inquiry


def inquiry(request, pk):
    """manages inquiry form submit and save data"""

    if request.method == "POST":

        car = Car.objects.get(pk=pk)
        if request.user.is_authenticated:
            user = CustomUser.objects.get(id=request.user.id)

            has_user_query = Inquiry.objects.all().filter(car=car, user=user)
            if has_user_query:
                messages.error(request, "You already have a query for this car,\
                                Please wait for the responce from us")
                return redirect("car", pk=pk)

            name = user.username
        else:
            user = None
            name = request.POST["name"]
        customer_query = request.POST["customer_query"]
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        comment = request.POST["message"]

        inquiry = Inquiry(user=user, car=car, name=name,
                          customer_query=customer_query, city=city, state=state,
                          email=email, phone=phone, comment=comment)

        # Now send Email
        admin_emails = ['nuruddinsayeed@gmail.com', ]
        send_mail(
            'New Car Inquiry',
            name + ' have some query about ' + car.car_title +
            '. Please login to your admin account to get detail',
            'nuruddinsayeed22@gmail.com',
            admin_emails,
            fail_silently=False,
        )

        inquiry.save()
        messages.success(request, "your request has been successfully submitted,\
                    we will get back to you soon")

        return redirect("car", pk=pk)
        # return redirect("/car/"+car.id)
