from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Car


@receiver(pre_save, sender=Car)
def set_max_price(sender, instance, *args, **kwargs):
    """Set max price automatically"""
    """Because of pre_save singal it will be called every time before
        Car object updated or created and here instance is the
        Car instance that is going to be created or updated"""

    if (Car.objects.filter(id=instance.id).exists() or instance.price != 0):
        old_price = Car.objects.get(id=instance.id).price

        if (old_price > instance.price or instance.max_price > instance.price):
            instance.max_price = max(old_price, instance.max_price)
        else:
            instance.max_price = 0
    else:
        instance.max_price = 0
