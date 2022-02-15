from django.db import models
from django.conf import settings
from login_signup.models.doctor import Doctor


class Appointment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, verbose_name="Lieu")

    def __str__(self):
        return f"{self.user} {self.doctor} {self.date} {self.time}"
