from django.conf.urls import url
from django.contrib import admin
from . import views

#<---------- app level ----- Travel ----------->

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addTripPage$', views.addTripPage, name='addTripPage'),
    url(r'^create$', views.create, name='create'),
]
