from django.conf.urls import url
from django.contrib import admin
from . import views

#<---------- app level ----- LoginReg ----------->

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^r_process$', views.r_process, name = 'products'),
    url(r'^l_process$', views.l_process, name = 'products'),
    url(r'^logout$', views.logout, name = 'logout'),
]
