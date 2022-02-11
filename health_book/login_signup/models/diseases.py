from django.db import models


class Diseases(models.Model):

    name = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=1000)
    cures = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
