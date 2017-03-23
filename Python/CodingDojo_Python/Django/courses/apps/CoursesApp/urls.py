from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^remove/(?P<id>\d+)$', views.remove), # (?P<id>\d+) has to match the id in a-href tag in the remove button in index.html
    url(r'^revert$', views.index),
    url(r'^destroy/(?P<id>\d+)$', views.destroy) # (?P<id>\d+) has to match the id in form action="destroy/{{ remv.id}}" in delete.html

]
