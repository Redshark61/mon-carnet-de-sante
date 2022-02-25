from django import template

register = template.Library()


def to_str(value):
    return str(value)


register.filter('to_str', to_str)
