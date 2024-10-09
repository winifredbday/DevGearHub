from django import template

register = template.Library()

@register.filter
def add(value, arg):
    try:
        return value + arg
    except TypeError:
        return value  # handle the case where value isn't a number
