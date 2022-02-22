from django.db import models
from django.conf import settings
from login_signup.models.diseases import Diseases


class UserDisease(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} {self.disease}"
