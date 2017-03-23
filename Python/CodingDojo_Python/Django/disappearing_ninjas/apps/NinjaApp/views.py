from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "ninjas/index.html")

def ninjas(request):

    context = {
    'displayAll' : True
    }

    return render(request, "ninjas/ninjas.html", context)

def show(request, color):

    context = {
    'displayAll' : False,
    'color' : color
    }

    return render(request, "ninjas/ninjas.html", context)
