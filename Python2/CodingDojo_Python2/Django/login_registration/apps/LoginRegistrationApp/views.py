from django.shortcuts import render, HttpResponse, redirect
from .models import User  # import ex Users, Books, Authors
from django.contrib import messages
from django.core.urlresolvers import reverse


def index(request):
    print "*" * 40
    print "index page of login registration "
    print "*" * 40
    return render(request,'LoginRegistrationApp/login_registration.html')

def register(request):
    # print "*" * 40
    # print "register page"
    # print "*" * 40

    data = {
        'fname': request.POST['first_name'],
        'lname': request.POST['last_name'],
        'email': request.POST['email'],
        'pass': request.POST['password'],
        'cpass': request.POST['cpassword'],
    }
    result = User.objects.validate(data)## this will push to models.py
    # print "1 " * 50
    if result[0]:
        # print "2 " * 50
        # request.session['user_id'] = result[1].id
        # print "7 " * 50
        # print request.session['user_id']
        return redirect(reverse("login:index"))
    else:
        for err in result[1]:
            messages.error(request,err)
        return redirect("/")

    return redirect("/")#login is from proj-lvl url,index is from app-lvl urls

def login(request):
    print "*" * 40
    print "login page"
    print "*" * 40

    data = {
        'email': request.POST['email'],
        'pass': request.POST['password'],
    }
    result = User.objects.login(data) # this will push to models.py
    print "22 " *40

    if result[0]:
        print "23 " *40
        request.session['user_id'] = result[1].id
        print request.session['user_id']
        print "24 " *40
        return redirect("/")

    return redirect("/")#login is from proj-lvl url,index is from app-lvl urls
