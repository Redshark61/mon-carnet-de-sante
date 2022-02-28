from django import template
from login_signup.models.notification import Notification

register = template.Library()


def to_str(value):
    return str(value)


def notification_message(value):
    notification = Notification.objects.filter(for_user=value)
    return notification


register.filter('to_str', to_str)
register.filter('notification_message', notification_message)
