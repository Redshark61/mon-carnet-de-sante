from django.db import models


class RPPS(models.Model):

    rpps = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rpps}"
