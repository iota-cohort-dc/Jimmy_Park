from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Clients, Projects

def index(request):

    return render(request,"ClientRes/index.html")

def addClientPage(request):

    return render(request,"ClientRes/addClient.html")

def addClient(request):
    if request.method == 'POST':
        if Clients.objects.filter(name=request.POST['name']):
            clientUser = Clients.objects.get(
                name = request.POST['name'],
                email = request.POST['email'],
                phone = request.POST['phone'],
                # notes = request.POST['notes']
                )
        else:
            clientUser = Clients.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                phone = request.POST['phone'],
                notes = request.POST['notes']
                )
        # context = {
        #     'client': Clients.objects.get(id=id)
        # }
        # return render(request,"ClientRes/showClient.html")
        return redirect(reverse("index:showClient", kwargs={'id': clientUser.id}))
    else:
        return redirect("/")

def showClient(request,id):

    context = {
        'name': Clients.objects.get(id=id),
        # 'project':
    }


    return render(request,"ClientRes/showClient.html",context)
