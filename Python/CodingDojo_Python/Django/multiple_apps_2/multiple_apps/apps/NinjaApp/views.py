from django.shortcuts import render, HttpResponse, redirect
# from django.contrib import messages
# from .models import User
from django.core.urlresolvers import reverse

def index(request):

    return render(request, "ninjas/index.html")

def ninjas(request):

    context = {
    'displayAll' : True
    }

    return redirect(reverse("teen_ninja:index"))

def show(request, color):

    context = {
    'displayAll' : False,
    'color' : color
    }

    return render(request, "ninjas/ninjas.html", context)
