from django.conf.urls import url, include ## CoursesApp
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = 'remove'), 
    url(r'^revert$', views.index, name = 'revert'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'destroy'),

]
