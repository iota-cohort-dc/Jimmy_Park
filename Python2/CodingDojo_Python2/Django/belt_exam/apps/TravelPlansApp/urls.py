from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'page'),
    url(r'^addTrip$', views.addTrip, name = 'addTrip'),
    url(r'^addTripPlan$', views.addTripPlan, name = 'addTripPlan'),
    # url(r'^success$', views.success, name = 'success'),
    # url(r'^logout$', views.logout, name = 'logout'),
]
