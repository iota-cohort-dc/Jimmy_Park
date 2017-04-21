from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse


def index(request):
	context = {
	'trips': Trips.objects.all()
	}
	return render(request, "TravelPlansApp/index.html", context)

def course(request):

	Course.objects.create(name=request.POST['name'], description=request.POST['desc'])

	return redirect('/')

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
