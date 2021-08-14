from django.db import models

from cars.models import Car
from users.models import CustomUser


class Inquiry(models.Model):
    """Define Inquiry Model Database"""

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=150)
    customer_query = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"{self.name}: ({self.car.car_title})"
