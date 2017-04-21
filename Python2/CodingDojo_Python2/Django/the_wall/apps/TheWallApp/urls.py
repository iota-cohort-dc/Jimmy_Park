from django.conf.urls import url
# from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index),
    # url(r'^register$', views.register),
    # url(r'^login$', views.login),
    # url(r'^dashboard$', views.dashboard),
    url(r'^addMessage$', views.addMessage),
    url(r'^addComment$', views.addComment),
]
