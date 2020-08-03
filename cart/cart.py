from django.conf import settings
from jewelry_store.models import Product


class Cart(object):
    def __init__(self, request):
        """Инициализация корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """Добавить продукт в корзину или обновить его количество"""
        product_id = str(product.id_product)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.get_latest_price())}
        self.cart[product_id]['quantity'] += quantity

    def check_product(self, id_prod):
        """Наличие продукта в корзине"""
        product_id = str(id_prod)
        if product_id in self.cart:
            return self.cart[product_id]['quantity']
        else:
            return False

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "изменённый", чтобы убедиться, что он сохранён
        self.session.modified = True

    def remove(self, product):
        """Удаление товара из корзины"""
        product_id = str(product.id_product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перебор элементов в корзине и получение продуктов из базы данных"""
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id_product__in=product_ids)
        for product in products:
            self.cart[str(product.id_product)]['product'] = product

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_keys(self):
        return self.cart.keys()

    def get_len(self):
        """Подсчёт всех товаров в корзине"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Подсчёт стоимости товаров в корзине"""
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Удаление корзины из сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
