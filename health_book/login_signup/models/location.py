from django.db import models
from django.conf import settings


class Location(models.Model):

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.postal_code}"
