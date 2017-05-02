"""belt_review2 URL Configuration

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
from django.conf import settings
from apps.BooksApp.models import Books, Authors, Reviews
from apps.LoginRegApp.models import User

# class UserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(User, UserAdmin)
#
# class BooksAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Books, BooksAdmin)
#
# class AuthorsAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Authors, AuthorsAdmin)
#
# class ReviewsAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Reviews, ReviewsAdmin)
#
# if settings.DEBUG:
#     import debug_toolbar

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^__debug__/', include('apps.LoginRegApp.urls')),
    url(r'^', include('apps.LoginRegApp.urls', namespace = 'login')),
    url(r'^books/', include('apps.BooksApp.urls', namespace='books')),
]
