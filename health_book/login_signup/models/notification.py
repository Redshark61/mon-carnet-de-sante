from django.db import models
from django.conf import settings


class Notification(models.Model):

    class NotificationType(models.TextChoices):
        MESSAGE = "M"
        NEW_PATIENT = "NP"

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, related_name='from_user')
    for_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='for_user')
    content = models.CharField(max_length=100, null=True, blank=True)
    notification_type = models.CharField(max_length=10, choices=NotificationType.choices)

    def __str__(self):
        return f"{self.from_user} {self.for_user} {self.content}"
