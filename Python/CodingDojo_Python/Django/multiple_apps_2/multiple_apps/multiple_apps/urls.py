"""multiple_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.MultAppsApp.urls', namespace = "login")),

    url(r'^courses/', include('apps.CoursesApp.urls', namespace = "courses")),

    url(r'^ninjaapp/', include('apps.NinjaApp.urls', namespace = "teen_ninja")),

    url(r'^ninjagoldapp/', include('apps.NinjaGoldApp.urls', namespace = "ninja_gold")),

    url(r'^timedisplay/', include('apps.timedisplay.urls', namespace = "time_display")),
]
