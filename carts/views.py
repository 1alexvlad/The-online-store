from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

def cart_add(request, product_slug):
# Получили запрос с product_slug
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
# Запрашиваем все корзины, которые есть у конкретному продукту
        carts = Cart.objects.filter(user=request.user, product=product)

# Если у пользователя уже был добавлен товар в корзину, то увеличиваем на 1
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quanity += 1
                cart.save()
# А если этого товара не было, то создаем новую корзину
        else:
            Cart.objects.create(user=request.user, product=product, quanity=1)
# HTTP_REFERER - отвечает за то с какой стр. попали
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    pass


def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    
    return redirect(request.META['HTTP_REFERER'])