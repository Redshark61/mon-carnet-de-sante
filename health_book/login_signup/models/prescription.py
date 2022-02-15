from django.db import models
from django.conf import settings
from login_signup.models.doctor import Doctor
from login_signup.models.treatment import Treatment


class Prescription(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.SET_NULL, null=True)
    prescription = models.TextField()
    end_date = models.DateField(null=True, blank=True)
    is_permanent = models.BooleanField(default=False)
