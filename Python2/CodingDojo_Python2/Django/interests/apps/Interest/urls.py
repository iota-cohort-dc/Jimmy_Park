from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addNewInterest$', views.addNewInterest, name='addNewInterest'),
    url(r'^users$', views.users, name='users'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
]
