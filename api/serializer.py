from rest_framework import serializers
from jewelry_store.models import Product, ProductPrice, Client, Status, Purchase


class ProductListSerializer(serializers.ModelSerializer):
    """Список изделий"""

    class Meta:
        model = Product
        fields = ("id_product", "title")


class PriceCreateSerializer(serializers.ModelSerializer):
    """Добавление цены товара"""

    class Meta:
        model = ProductPrice
        exclude = ("id", )

    def create(self, validated_data):
        one_price = ProductPrice.objects.create(
            product=validated_data.get('product'),
            price=validated_data.get('price')
        )
        return one_price


class PriceListSerializer(serializers.ModelSerializer):
    """Цены"""

    class Meta:
        model = ProductPrice
        exclude = ("id", "product")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Изделие"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    material = serializers.SlugRelatedField(slug_field="name", read_only=True)
    gems = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    prices = PriceListSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class StatusListSerializer(serializers.ModelSerializer):
    """Список статусов"""

    class Meta:
        model = Status
        fields = "__all__"


class StatusCreateSerializer(serializers.ModelSerializer):
    """Создать статус"""

    class Meta:
        model = Status
        fields = "__all__"

    def create(self, validated_data):
        one_status = Status.objects.create(
            purchase=validated_data.get('purchase'),
            status=validated_data.get('status')
        )
        return one_status


class PurchaseListSerializer(serializers.ModelSerializer):
    """Список покупок"""
    class Meta:
        model = Purchase
        fields = "__all__"


class PurchaseDetailSerializer(serializers.ModelSerializer):
    """Покупка"""

    statuses = StatusListSerializer(many=True)

    class Meta:
        model = Purchase
        fields = "__all__"
