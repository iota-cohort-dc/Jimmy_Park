from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from .models import Travels
from django.core.urlresolvers import reverse
from django.db.models import Q
from ..LoginReg.models import User

def index(request):
    context = {
        'trips': Travels.objects.filter(Q(userplanning_id = request.session['user_id']) | Q(userjoining = request.session['user_id'])),
        'plans': Travels.objects.all().exclude(Q(userplanning_id = request.session['user_id']) | Q(userjoining = request.session['user_id'])),
        'users': User.objects.all(),
    }
    return render(request,"Travel/index.html", context)

def addTripPage(request):
    return render(request,"Travel/addTrip.html")

def create(request):
    result = Travels.objects.validate(request.POST, request.session['user_id'])
    print "*" *30
    print result
    print "*" *30
    if result[0]:
        return redirect(reverse('travel:index'))
    else:
        for errs in result[1]:
            # message.errors(request, errs)
            return redirect(reverse('travel:addTripPage'))

    return redirect(reverse("travel:addTripPage"))

def joinTrip(request):
    return redirect("/")

def showTripsPage(request):

    return render(request,"Travel/showTripsPage.html")
