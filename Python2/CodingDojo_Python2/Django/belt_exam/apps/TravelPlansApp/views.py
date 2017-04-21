from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Trips
from django.core.urlresolvers import reverse


def index(request):
	context = {
	'trips': Trips.objects.all()
	}
	return render(request, "TravelPlansApp/index.html", context)

def addTrip(request):

    data = {
        'allTrips': Trips.objects.all(),
    }

    return render(request,"TravelPlansApp/addTrip.html")

def addTripPlan(request):


    user_id = request.session['user']
    # print "WMYVA" * 20
    print user_id
    # user = User.object.get(id = user_id)

    print "=0=0" * 20
    # print user
    print "=0=0" * 20


    Trips.objects.create(
        destination = request.POST['destination'],
        travelStart = str(request.POST['travelStart']),
        travelEnd = str(request.POST['travelEnd']),
        description = request.POST['description'],
        # user = request.session['user'],
        # user = User.object.get(id = user_id)
    )


    return redirect(reverse('plans:page'))



# def remove(request, id):
# 	context = {
# 	'cors': Course.objects.get(id=id)
# 	}
# 	return render(request, "CoursesApp/delete.html", context)
#
# def delete(request, id):
#
# 	Course.objects.get(id=id).delete()
#
# 	return redirect('/')
