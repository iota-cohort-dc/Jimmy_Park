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
	'plans': Trips.objects.all().exclude(Q(planned_user_id=request.session['user_id']) | Q(joining_user =request.session['user_id'])),
	'users': User.objects.all(),
	}
	return render(request, "TravelPlansApp/index.html", context)

def addTrip(request):
    return render(request,"TravelPlansApp/addTrip.html")

def createTrip(request):
	user = User.objects.get(id=request.session['user_id'])
	result = Trips.objects.addNewTrip(request.POST,user.id)

	# if result[0] == False:
	# 	print "False"
	# return redirect(reverse('plans:addTripPlan'))
	#
	# else:
	return redirect(reverse('plans:page'))

def joinTrip(request,id):
	joining = User.objects.get(id=request.session['user_id'])
	trip_joining = Trips.objects.get(id=id)
	trip_joining.joining_user.add(joining)
	return redirect(reverse('plans:page'))

def showTripPage(request,id):
	# print "#$%^" * 20
	trips = Trips.objects.get(id=id)
	context = {
		'trips': Trips.objects.get(id = id),
		'planner': User.objects.get(id = trips.planned_user.id),
		'joiningusers': trips.joining_user.all(),
	}
	# print context
	# print "#$%^" * 20

	return render(request,"TravelPlansApp/destination.html", context)
