from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^qindex$', views.index, name = 'qindex'),
    url(r'^addQuote$', views.addQuote, name = 'addQuote'),
    url(r'^addFavorite/(?P<id>\d+)$', views.addFavorite, name = 'addFavorite'),
    url(r'^removeFavorite/(?P<id>\d+)$', views.removeFavorite, name = 'removeFavorite'),
    url(r'^userInfoPage/(?P<id>\d+)$', views.userInfoPage, name = 'userInfoPage'),
]
