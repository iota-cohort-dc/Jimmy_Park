from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process, name='process'),
    url(r'^join_friends$', views.join_friends, name='join_friends'),


]
