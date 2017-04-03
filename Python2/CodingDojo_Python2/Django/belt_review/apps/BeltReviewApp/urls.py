from django.conf.urls import url, include
#from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^register$', views.validate),
    url(r'^login$', views.success),
    url(r'^logout$', views.logout, name='logout')
]
