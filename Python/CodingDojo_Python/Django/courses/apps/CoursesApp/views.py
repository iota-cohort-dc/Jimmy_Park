from django.shortcuts import render, HttpResponse, redirect
from .models import Courses # Courses is from the models.py

def index(request):
    # context dictionary
    context = {
    "courses" : Courses.objects.all()
    # select all from Courses
    }

    return render(request, ("CoursesApp/index.html"), context)

def create(request):
    # use the ORM..............
    Courses.objects.create(name=request.POST['name'],description=request.POST['description'])
    # above is saying insert the Courses, (name, description.. created_at,updated_at ) values of (name, description, now(), now())
    return redirect('/')

def remove(request, id): # have to put id, next request bc you are going to use it below

    context = {
    'remv' : Courses.objects.get(id=id) # any variable name is ok.. this case was 'remv'.. remove was used in the a-href in the index.html and also in the form action="/..... /{{ remv.id }}"
    }

    return render(request, "CoursesApp/delete.html", context)


def destroy(request, id):

    Courses.objects.get(id=id).delete()

    return redirect("/")
