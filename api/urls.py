from api import views
from django.urls import path, include


urlpatterns = [
    path("get_product/", views.ProductListView.as_view()),
    path("get_product/<int:pk>", views.ProductDetailView.as_view()),
    path('create_price/', views.PriceCreateView.as_view()),
    path('get_status/', views.StatusListView.as_view()),
    path('create_status/', views.StatusCreateView.as_view()),
    path('get_purchase/', views.PurchaseListView.as_view()),
    path('get_purchase/<int:pk>', views.PurchaseDetailView.as_view()),
]
