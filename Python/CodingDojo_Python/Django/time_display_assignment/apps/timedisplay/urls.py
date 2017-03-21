from django.conf.urls import url, include
from . import views

# def index (request):
#     return

urlpatterns = [
    url(r'^$', views.index),
]

# print "I will be your future routes; HTTP requests will be captured by me."
