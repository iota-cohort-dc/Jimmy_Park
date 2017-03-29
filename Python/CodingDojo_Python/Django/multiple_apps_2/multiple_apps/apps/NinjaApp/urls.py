from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^ninjas$', views.ninjas, name = 'ninjas'),
    url(r'^ninjas/(?P<color>\w+)$', views.show, name = 'ninja_show')
]
