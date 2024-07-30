import main.views
from django import template


register = template.Library()


@register.simple_tag()
def get_categories():
    return main.views.categories