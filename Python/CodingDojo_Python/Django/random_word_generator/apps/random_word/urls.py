from django.conf.urls import url, include
from . import views

# def index (request):
#     return

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate$', views.generate)
]
