from django.db import models
from datetime import date


# Create your models here.
from django.urls import reverse


class Material(models.Model):
    """Материалы"""
    name = models.CharField("Имя", max_length=149)
    probe = models.PositiveSmallIntegerField("Проба", default=0)

    def __str__(self):
        return f"{self.name}, {self.probe}"

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class Gems(models.Model):
    """Драгоценные камни"""
    id_gem = models.AutoField("Номер вставки", primary_key=True)
    name = models.CharField("Камень", max_length=149, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Драгоценный камень"
        verbose_name_plural = "Драгоценные камни"


class Client(models.Model):
    """"Клиент"""
    name = models.CharField("Имя", max_length=149)
    email = models.EmailField()
    phone = models.CharField("Телефон", max_length=16)

    def __str__(self):
        return f"{self.name}, {self.phone}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class CategoriesProduct(models.Model):
    """Категории"""
    # parent_category = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL,
    #                                     blank=True, null=True)
    name = models.CharField("Категория", max_length=149)
    url = models.SlugField(max_length=199, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_list", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """"Продукты"""
    id_product = models.AutoField("Артикул", primary_key=True)
    category = models.ManyToManyField(CategoriesProduct, verbose_name="Категория", related_name="product_categories")
    material = models.ForeignKey(Material, verbose_name="Материал", on_delete=models.SET_NULL, null=True)
    gems = models.ManyToManyField(Gems, verbose_name="Драгоценные камни", related_name="product_gems", blank=True)
    with_gems = models.BooleanField("Со вставками", default=True)
    title = models.CharField("Название", max_length=149)
    amount_storage = models.PositiveIntegerField("Количество товара на складе", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="products/")
    url = models.SlugField(max_length=199, unique=True)
    weight_material = models.FloatField("Вес металла", default=0, help_text="граммы")
    weight_one_gem = models.FloatField("Вес одного камня", default=0, help_text="караты")
    amount = models.PositiveSmallIntegerField("Количество камней (данного типа)", default=0)

    def __str__(self):
        return f"Артикул: {self.id_product} ({self.title})"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})

    def get_stone(self):
        return self.gems.first()

    def get_latest_price(self):
        return self.prices.latest('date').price

    get_latest_price.short_description = "Цена"

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"


class Purchase(models.Model):
    """"Покупка"""
    id_purchase = models.AutoField("Номер покупки", primary_key=True)
    client = models.OneToOneField(Client, verbose_name="Номер клиента", on_delete=models.CASCADE)
    date = models.DateField("Дата покупки", default=date.today)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_latest_status(self):
        return self.statuses.latest('date').status

    def __str__(self):
        return f"{self.id_purchase}, {self.client}"

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    get_latest_status.short_description = "Статус"


class AllPurchases(models.Model):
    """"Все покупки"""
    purchase = models.ForeignKey(Purchase, verbose_name='Заказ', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, verbose_name='Изделие', on_delete=models.CASCADE, related_name='order_items')
    price = models.PositiveIntegerField("Цена", default=0, help_text="руб.")
    amount = models.PositiveSmallIntegerField("Количество товара", default=0)

    def __str__(self):
        return f"{self.purchase}"

    def get_cost(self):
        return self.price * self.amount

    class Meta:
        verbose_name = "Все покупки"
        verbose_name_plural = "Все покупки"
        constraints = [
            models.UniqueConstraint(fields=['product', 'purchase'], name='unique purchases')
        ]


class ProductPrice(models.Model):
    """Цены"""
    product = models.ForeignKey(Product, verbose_name="Номер продукта", on_delete=models.CASCADE, related_name='prices')
    date = models.DateField("Дата изменения", auto_now_add=True)
    price = models.PositiveIntegerField("Цена", default=0, help_text="руб.")

    def __str__(self):
        return f"{self.product} {self.date} {self.price}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        constraints = [
            models.UniqueConstraint(fields=['product', 'date'], name='unique price')
        ]


class Status(models.Model):
    """Статус покупки"""
    purchase = models.ForeignKey(Purchase, verbose_name="Номер покупки",
                                 on_delete=models.CASCADE, related_name='statuses')
    date = models.DateTimeField("Дата изменения", auto_now_add=True)
    status = models.BooleanField(verbose_name='Статус заказа', default=False)

    def __str__(self):
        return f"{self.purchase} {self.date} {self.status}"

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        constraints = [
            models.UniqueConstraint(fields=['purchase', 'date'], name='unique status')
        ]
