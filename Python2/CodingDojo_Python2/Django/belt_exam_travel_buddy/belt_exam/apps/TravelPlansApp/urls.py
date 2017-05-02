from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'page'),
    url(r'^addTrip$', views.addTrip, name = 'addTrip'),
    url(r'^createTrip$', views.createTrip, name = 'addTripPlan'),
    url(r'^joinTrip/(?P<id>\d+)$', views.joinTrip, name = 'joinTrip'),
    url(r'^showTrip/(?P<id>\d+)$', views.showTripPage, name = 'showTripPage'),

]
