from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Trips, User
from ..TravelBuddyApp.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
import datetime
from time import gmtime, strftime

def index(request):
	context = {  # Q and | allow me to do compare two columns
	'trips': Trips.objects.filter(Q(planned_user_id=request.session['user_id']) | Q(joining_user =request.session['user_id'])),
	# for the user who's logged in:  -- I planned the trip ((or)) I joined the trip --
	'plans': Trips.objects.all().exclude(Q(planned_user_id=request.session['user_id']) | Q(joining_user =request.session['user_id'])),
	# for the user who's logged in:  -- I DIDN'T plan the trip ((or)) I DIDN'T join the trip --
	'users': User.objects.all(),
	}
	return render(request, "TravelPlansApp/index.html", context)

def addTrip(request):
    return render(request, "TravelPlansApp/addTrip.html")

def createTrip(request):
	result = Trips.objects.addNewTrip(request.POST, request.session['user_id'])

	if result[0]: # True Trip was made correctly
		return redirect(reverse("plans:page"))

	else: # Trip wasn't created successfully, and should put errors into messages framework, and then run messages loop after redirecting to addTrip.html
		for errs in result[1]:
			messages.error(request, errs)
		return redirect(reverse("plans:addTrip"))

def joinTrip(request,id):
	joining = User.objects.get(id=request.session['user_id'])
	trip_joining = Trips.objects.get(id=id)
	trip_joining.joining_user.add(joining)
	return redirect(reverse('plans:page'))

def showTripPage(request,id):

	context = {
		'trips': Trips.objects.get(id = id),
		'planner': User.objects.get(id = trips.planned_user.id),
		'joiningusers': trips.joining_user.all(),
	}

	return render(request,"TravelPlansApp/destination.html", context)
