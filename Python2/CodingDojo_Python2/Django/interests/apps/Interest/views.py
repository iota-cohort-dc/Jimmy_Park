
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Users, Interests, UsersInterest

def index(request):
    print "*" * 20,"home page ", "*" * 20
    return render(request,"Interest/index.html")

def addNewInterest(request):
    print "*" *20,"add new interest ", "*" * 20
    # results = UsersInterest.objects.addInterest(request.POST)#user_id
    # if results[0]:
    if request.method == 'POST':
        if Users.objects.filter(name=request.POST['name']):
            user = Users.objects.get(name=request.POST['name'])
        else:
            user = Users.objects.create(name=request.POST['name'])
        if Interests.objects.filter(interest=request.POST['interest']):
            interest = Interests.objects.get(interest=request.POST['interest'])
        else:
            interest = Interests.objects.create(interest=request.POST['interest'])

        UsersInterest.objects.create(user=user, interest=interest)

        return redirect(reverse("interest:users"))
    else:
        # for errs in results[1]:
            # message.error(request, errs)
        return redirect("/")
    # return render(request,"Interests/users.html")

def users(request):
    print "users page"
    context = {
        'user': Users.objects.all(),
    }
    return render(request,"Interest/users.html", context)

def show(request,id):
    print "*" * 20,"show page","*" * 20

    data = {
    'interest': UsersInterest.objects.filter(user_id=id),
    'user': Users.objects.get(id=id)
    }
    return render(request,"Interest/show.html", data)
