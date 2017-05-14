from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index$', views.index, name = 'index'),
    url(r'^addProductPage$', views.addProductPage, name = 'addProductPage'),
    url(r'^addProduct$', views.addProduct, name = 'addProduct'),
    url(r'^joinWish/(?P<id>\d+)$', views.joinWish, name = 'joinWish'),
    url(r'^showProduct/(?P<id>\d+)$', views.showProduct, name = 'showProduct'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = 'remove'),
]
