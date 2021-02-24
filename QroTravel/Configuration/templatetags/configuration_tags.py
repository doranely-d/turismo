from django.conf import settings as dj_settings
from django import template

import re

register = template.Library()


@register.filter(name='settings')
def settings(attribute):
    return getattr(dj_settings, attribute, '')


@register.filter(name='no_slash')
def no_slash(string):
    return string.rstrip('/')


@register.filter(name='no_protocol')
def no_protocol(string):
    return string.lstrip('http://').lstrip('https://')


@register.filter('fieldtype')
def fieldtype(field):
    return field.field.widget.input_type


@register.filter('zfill')
def zfill(string, value):
    try:
        return str(string).zfill(int(value))
    except:
        return string


@register.filter(name='only_numbers')
def only_numbers(string):
    return re.sub('\D', '', string)
