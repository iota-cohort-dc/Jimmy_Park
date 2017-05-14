from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):

    return render(request, 'LoginReg/index.html')

def r_process(request):  ### validate ###

    data = {
    "name" : request.POST['name'],
    "alias" : request.POST['alias'],
    # "email" : request.POST['email'],
    "pass" : request.POST['pass'],
    "c_pass" : request.POST['c_pass'],
    "birth_date": request.POST['birth_date']
    }
    # print "*" * 30
    result = User.objects.validate(data)

    if result[0]:
        request.session['user_id'] = result[1].id
        messages.success(request, "Success! ")
        # messages.success(request)
        print "=+" * 50
        print result[0]
        print "=+" * 50
        return redirect("/")
    else:
        for err in result[1]:
            print "$" * 50
            print result[1]
            print "$" * 50
            messages.error(request, err)
        return redirect("/")

def l_process(request): ### success ###

    if request.method == 'POST':
        alias = request.POST['alias']
        password = request.POST['pass']
        if not User.objects.filter(alias=alias):
            context = {
                'error': 'Email not found'
            }
            print "** ||||" * 20
            return render(request, 'LoginReg/index.html', context)

        user = User.objects.filter(alias=alias)

        if bcrypt.hashpw(str(password), str(user[0].password)) == user[0].password:
            request.session['user_id'] = user[0].id
            #this put user IN session
        else:
            context = {
                'pass': 'Password not valid'
            }
            #this did NOT put user in session
            print "% " * 20
            return render(request, 'LoginReg/index.html', context)

        print "###==" * 20
        # return redirect(reverse('plans:page'))
        return redirect(reverse('wishList:index')) #### change this to the new site quotes


def logout(request):
    print "^" * 20
    request.session.clear()
    print "-" * 20
    return redirect("/")
