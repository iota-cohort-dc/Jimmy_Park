from django.shortcuts import render, HttpResponse, redirect
from .models import User  # import ex Users, Books, Authors
from django.contrib import messages
from django.core.urlresolvers import reverse


def index(request):
    print "*" * 40
    print "index page of login registration "
    print "*" * 40
    return render(request,'login_registration.html')

def register(request):
    print "*" * 40
    print "register page"
    print "*" * 40

    data = {
        'fname': request.POST['first_name'],
        'lname': request.POST['last_name'],
        'email': request.POST['email'],
        'pass': request.POST['password'],
        'cpass': request.POST['cpassword'],
    }
    return redirect(reverse,'login:index')#login is from proj-lvl url,index is from app-lvl urls

def login(request):
    print "*" * 40
    print "login page"
    print "*" * 40

    data = {
        'email': request.POST['email'],
        'pass': request.POST['password'],
    }

    return redirect(reverse,'login:index')#login is from proj-lvl url,index is from app-lvl urls
