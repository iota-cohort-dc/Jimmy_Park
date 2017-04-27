from django.shortcuts import render, redirect
from .models import User, Friend

def index(request):
    friends = Friend.objects.all()
    users = User.objects.all()
    context = {
        'friends': friends,
        'users': users,
    }
    return render(request,"ManyFriends/index.html", context)

def process(request):
    name = request.POST['create']
    User.objects.create(name=name)
    return redirect("/")

def join_friends(request):
    friend1 = request.POST['friend_1']
    friend2 = request.POST['friend_2']
    Friend.objects.create(name_id=friend1, friend_id=friend2)

    return redirect("/")
