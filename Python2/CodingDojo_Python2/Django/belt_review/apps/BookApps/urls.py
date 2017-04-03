from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^addBook$', views.review, name='addBook'),
    url(r'^displayRev/(?P<id>\d+)$', views.displayRev, name='displayRev'),
    url(r'^userPage/(?P<id>\d+)$', views.userPage, name='userPage'),
]
