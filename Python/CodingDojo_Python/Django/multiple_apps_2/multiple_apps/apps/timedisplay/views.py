from django.shortcuts import render, HttpResponse
import datetime


def index(request):
    print datetime.datetime.now()
    context = {
        'currentTime': datetime.datetime.now()
    }

    return render(request, "timedisplay/index.html", context)
# Create your views here.
