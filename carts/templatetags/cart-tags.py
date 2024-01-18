from django import template

from carts.models import Cart



register = template.Library()

@register.simple_tag()
def user_carts(requst):
    if requst.user.is_authenticated:
        return Cart.objects.filter(user=requst.user)