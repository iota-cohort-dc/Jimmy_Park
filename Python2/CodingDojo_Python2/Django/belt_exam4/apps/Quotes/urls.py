from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^qindex$', views.index, name = 'qindex'),
    url(r'^addQuote$', views.addQuote, name = 'addQuote'),
    url(r'^addFavorite$', views.addFavorite, name = 'addFavorite'),
    # url(r'^addComment$', views.addComment, name = 'addComment'),
]
