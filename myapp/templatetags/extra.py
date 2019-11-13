from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='get_index')
def get_index(value, index):
    return value.index
