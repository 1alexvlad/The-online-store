from django.db import models
from goods.models import Products

from users.models import User


class CartQuerySet(models.QuerySet):
    
# будем искать итогую сумму по каждому отдельному товару
    def total_price(self):
        return sum(cart.product_price() for cart in self)

# общее кол-во товаров
    def total_quanity(self):
        if self:
            return sum(cart.quanity for cart in self)
        return 0

class Cart(models.Model):
# Добавил blank=True, null=True - для того чтобы не авторизированный пользователь мог добавлять в корзину товары
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quanity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
# Если пользователь не авторизированный, то будем вносить данные не по user, а по полю session_key
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина' 
        verbose_name_plural = 'Корзины' 

    objects = CartQuerySet().as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quanity , 2)

    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quanity}'
