from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Clients, Projects

def index(request):
    pass
    return render(request,"ClientRes/index.html")

def addClientPage(request):

    return render(request,"ClientRes/addClient.html")

def addClient(request):
    if request.method == 'POST':
        if Clients.objects.filter(name=request.POST['name']):
            clientUser = Clients.objects.get(name=request.POST['name'])
        else:
            clientUser = Client.objects.create(name=request.POST['name'])

    return render(request,"ClientRes/addClient.html")
