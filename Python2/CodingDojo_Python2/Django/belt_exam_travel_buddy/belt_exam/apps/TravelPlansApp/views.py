from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Trips, User
from ..TravelBuddyApp.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
import datetime
from time import gmtime, strftime


def index(request):
	context = {
	'trips': Trips.objects.filter(Q(planned_user_id=request.session['user_id']) | Q(joining_user =request.session['user_id'])),
	'plans':
	# get all trips where the creator or joined user isn't the user that's logged in. Q and | allow me to do compare two columns
	Trips.objects.all().exclude(Q(planned_user_id=request.session['user_id']) | Q(joining_user =request.session['user_id'])),
	'users': User.objects.all(),
	}
	return render(request, "TravelPlansApp/index.html", context)

def addTrip(request):
    return render(request, "TravelPlansApp/addTrip.html")

def createTrip(request):
	# user = User.objects.get(id=request.session['user_id'])
	result = Trips.objects.addNewTrip(request.POST, request.session['user_id'])
	# print result[0]
	# print result[1]
	# after the above code has been run, then result will either include True OR False and errs

	if result[0]:
		return redirect(reverse("plans:page"))
	# True Trip was made correctly

	else:
	# Trip wasn't created successfully, and should put errors into messages framework, and then run messages loop after redirecting to addTrip.html
		for errs in result[1]:
			messages.error(request, errs)
		return redirect(reverse("plans:addTrip"))


	# return redirect(reverse('plans:page'))

def joinTrip(request,id):
	joining = User.objects.get(id=request.session['user_id'])
	trip_joining = Trips.objects.get(id=id)
	trip_joining.joining_user.add(joining)
	return redirect(reverse('plans:page'))

def showTripPage(request,id):
	# print "#$%^" * 20

	context = {
		'trips': Trips.objects.get(id = id),
		'planner': User.objects.get(id = trips.planned_user.id),
		'joiningusers': trips.joining_user.all(),
	}
	# print context
	# print "#$%^" * 20

	return render(request,"TravelPlansApp/destination.html", context)
