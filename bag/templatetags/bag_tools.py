from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate item subtotal in bag.
    From CI Boutique Ado walkthrough.
    """
    return price * quantity
