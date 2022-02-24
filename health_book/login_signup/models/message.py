from django.conf import settings
from django.db import models
from login_signup.models import Doctor


class Message(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                               related_name='sender', null=True)
    destination = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='destination', null=True)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
