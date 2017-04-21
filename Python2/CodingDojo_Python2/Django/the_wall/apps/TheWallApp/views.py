from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Users, Comments, Messages

# Create your views here.
def index(request):

    all_users = Users.object.all()
    all_messages = Messages.object.all()
    context = {
        'users': all_users,
        'messages': all_messages,
    }


    return render(request, 'TheWallApp/wall_dashboard.html', context)

# def register(request):
#
#     return redirect(request, '/')
#
# def login(request):
#
#     return render(request,'/TheWallApp/wall_dashboard.html')
#
# def logout(request):
#
#     return redirect(request,'/')

def addMessage(request):
    print "*" * 40
    print "You've reached addMessage in views.py"
    print "*" * 40
    user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'], email = request.POST['email'])
    results = Message.object()
    print user

    return redirect('/')

def addComment(request):
    print "+=" * 20
    print "You've reached addMessage in views.py"
    print "+=" * 20
    return redirect('/')
