from django import template
from math import floor

register = template.Library()

@register.simple_tag()
def sale_price(price, discount):
    return floor(price - (price * discount * 0.01))

@register.simple_tag
def get_active_class(active_category, category):
    if active_category is None and category == '':
        return ' active'

    if active_category is None:
        return ''

    if active_category == category:
        return ' active'

    if active_category != category:
        return ''