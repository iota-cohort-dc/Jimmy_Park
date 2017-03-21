from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index)
]


  # from django.conf.urls import url
  # from . import views           # This line is new!
  # urlpatterns = [
  #   url(r'^$', views.index)     # This line has changed!
  # ]

# from django.conf.urls import url
# def method_to_run(request):
#     print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
#     print "By the way, here's the request object that Django automatically passes us:", request
#     print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
#
# urlpatterns = [
#     url(r'^$', method_to_run)
# ]

# print "I will be your future: HTTP request will be captured by me."
