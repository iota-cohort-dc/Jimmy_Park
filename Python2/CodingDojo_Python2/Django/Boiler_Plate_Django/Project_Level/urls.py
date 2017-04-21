from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.BeltReviewApps.urls', namespace = 'index')),
    url(r'^rename_this_route/', include('apps.BookApps.urls', namespace = 'need_to_rename_this')),

]
