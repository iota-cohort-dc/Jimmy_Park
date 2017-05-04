from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addClientPage$', views.addClientPage, name='addClientPage'),
    url(r'^addClient$', views.addClient, name='addClient'),
]
