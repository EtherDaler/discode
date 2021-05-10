from django import template

register = template.Library()


def default_image(queryset):
    return queryset.get(default=True).image.url

register.filter('default_image', default_image)