from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^addbook$', views.addbook, name = 'addbook'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^reviews$', views.reviews, name = 'reviews'),
    url(r'^user$', views.userpage, name = 'userpage'),
]
