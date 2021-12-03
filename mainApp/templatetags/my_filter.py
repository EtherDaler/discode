from django import template
from django.utils import timezone
from django.utils.translation import gettext as _

register = template.Library()

def create_range(value, start_index=0):
    return range(start_index, int(value) + start_index)

def star_space(value, start_index=0):
    res = 5 - int(value)
    return range(start_index, 5 - int(value))

def filter_items(value):
    now = timezone.now()
    number = value.filter(date_of_finish__gte=now).count()
    return number

register.filter('create_range', create_range)

register.filter('star_space', star_space)

register.filter('filter_items', filter_items)