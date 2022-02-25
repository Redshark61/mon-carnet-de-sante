from django.db import models
from django.conf import settings


class Notification(models.Model):

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, related_name='from_user')
    for_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='for_user')
    content = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.from_user} {self.for_user} {self.content}"
