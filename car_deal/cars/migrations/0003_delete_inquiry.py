# Generated by Django 3.2.6 on 2021-08-14 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_inquiry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inquiry',
        ),
    ]