from django.conf.urls import url
from cart import views
from django.urls import path, include


urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<pk>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<pk>\d+)/$', views.cart_remove, name='cart_remove'),
]
