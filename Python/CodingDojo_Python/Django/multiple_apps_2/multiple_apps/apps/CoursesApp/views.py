from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from .models import Courses, LoginReg

from django.db.models import Count

from django.core.urlresolvers import reverse

def index(request):

    context = {
    "courses" : Courses.objects.all()
    }

    return render(request, "CoursesApp/index.html", context)

def create(request):

    Courses.objects.create(name=request.POST['name'],description=request.POST['description'])

    return redirect(reverse("courses:index"))

def remove(request, id):

    context = {
    'user' : Courses.objects.get(id=id)
    }
    return render(request,"CoursesApp/delete.html", context)

def destroy(request, id):

    Courses.objects.get(id=id).delete()

    return redirect(reverse("courses:index"))

def addCourse(request):

    Course.objects.create(name=request.POST['name'], description=request.POST['desc'])

    return render(request, "CoursesApp/user_course.html")

def choose(request):


    context = {
        "cors": Courses.objects.all().annotate(num_users=Count('all_courses')),
        "user": User.objects.all() # goes into jinja for loop in html
    }

    return render (request, 'CoursesApp/users_courses.html', context)

def registerUser(request): # dorian said that this does not do anything. This is a GET. But does not go anywhere from here.

        user = User.objects.get(id=request.POST['Users'])
        course = Courses.objects.get(id=request.POST['Courses'])
        login = LoginReg.objects.create(user=user, course=course)

        return redirect(reverse('courses:choose'))
