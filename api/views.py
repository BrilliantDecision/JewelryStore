from rest_framework.response import Response
from rest_framework.views import APIView
from jewelry_store.models import Product, ProductPrice, Client, Status, Purchase
from api.serializer import ProductListSerializer, ProductDetailSerializer, PriceCreateSerializer, StatusListSerializer,\
    StatusCreateSerializer, PurchaseListSerializer, PurchaseDetailSerializer
# Create your views here.


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        products = Product.objects.get(id_product=pk)
        serializer = ProductDetailSerializer(products)
        return Response(serializer.data)


class PriceCreateView(APIView):
    def post(self, request):
        serializer = PriceCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class StatusListView(APIView):
    def get(self, request):
        statuses = Status.objects.all()
        serializer = StatusListSerializer(statuses, many=True)
        return Response(serializer.data)


class StatusCreateView(APIView):
    def post(self, request):
        serializer = StatusCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class PurchaseListView(APIView):
    def get(self, request):
        purchases = Purchase.objects.all()
        serializer = PurchaseListSerializer(purchases, many=True)
        return Response(serializer.data)


class PurchaseDetailView(APIView):
    def get(self, request, pk):
        purchase = Purchase.objects.get(id_purchase=pk)
        serializer = PurchaseDetailSerializer(purchase)
        return Response(serializer.data)
