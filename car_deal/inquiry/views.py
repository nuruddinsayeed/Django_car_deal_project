from django.contrib import messages
from django.shortcuts import redirect

from cars.models import Car
from users.models import CustomUser
from inquiry.models import Inquiry


def inquiry(request, pk):
    """manages inquiry form submit and save data"""

    if request.method == "POST":
        if request.user.is_authenticated:
            user = CustomUser.objects.get(id=request.user.id)
            name = user.username
        else:
            user = None
            name = request.POST["name"]
        customer_query = request.POST["customer_query"]
        car = Car.objects.get(pk=pk)
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        comment = request.POST["message"]

        inquiry = Inquiry(user=user, car=car, name=name,
                          customer_query=customer_query, city=city, state=state,
                          email=email, phone=phone, comment=comment)

        inquiry.save()
        messages.success(request, "your request has been successfully submitted,\
                    we will get back to you soon")

        return redirect("car", pk=pk)
        # return redirect("/car/"+car.id)
