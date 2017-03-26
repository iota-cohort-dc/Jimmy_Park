from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^r_process$', views.r_process),
    url(r'^l_process$', views.l_process),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]
