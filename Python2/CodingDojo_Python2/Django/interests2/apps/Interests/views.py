
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Users, Interests

def index(request):
    print "home page " * 10
    return render(request,"Interests/index.html")

def addNewInterest(request):
    print "add new interest " * 10
    # user_id = Users.objects.get(id=user_id)
    # print user_id
    results = Interests.objects.addInterest(request.POST)#user_id
    if result[0]:
        join = Users.objects.get(id=user_id)
        print "join"
        print "*" * 30
        interest_join = Interests.objects.get(id=id)
        print "interest_join"
        print "*" * 30
        joiningInterests.interest_join.add(join)
        print "=+" * 30

        return redirect(reverse("interest:users"))
    else:
        for errs in result[1]:
            # message.error(request, errs)
            return redirect("/")

    # return render(request,"Interests/users.html")

def users(request):
    print "users page"
    context = {
        'user': Users.objects.all(),
        'interest': Interests.objects.all(),
    }
    return render(request,"Interests/users.html", context)

def show(request):
    print "show page"
    data = {

    }
    return render(request,"Interests/show.html", data)
