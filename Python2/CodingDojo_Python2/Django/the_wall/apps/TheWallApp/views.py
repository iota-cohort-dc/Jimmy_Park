from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, '/TheWallApp/index.html')

def register(request):

    return redirect(request, '/')

def login(request):

    return render(request,'/TheWallApp/wall_dashboard.html')

def logout

    return redirect(request,'/')

def addMessage(request):

    return redirect(request,'/dashboard')

def addComment(request):

    return redirect(request,'/dashboard')
