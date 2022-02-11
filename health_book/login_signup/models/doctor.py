from django.db import models
from django.conf import settings
from login_signup.models.rpps import RPPS
from login_signup.models.job import Job


class Doctor(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rpps = models.ForeignKey(RPPS, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
