from django.db import models


class Team(models.Model):
    """Define Team data model for Executive Team"""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # year/mont/date
    facebook_profile = models.URLField(max_length=200)
    twitter_profile = models.URLField(max_length=200)
    google_plus_profile = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
