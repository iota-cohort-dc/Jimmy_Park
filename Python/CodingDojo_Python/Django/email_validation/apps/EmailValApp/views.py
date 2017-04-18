from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'lr_templates/index.html')

def r_process(request):
    # data = {
    # "first_name" : request.POST['first'],
    # "last_name" : request.POST['last'],
    # "email" : request.POST['email'],
    # "pass" : request.POST['pass'],
    # "c_pass" : request.POST['c_pass']
    # }

    result = User.objects.validate(data)
    if result[0]:
        # print "*" * 20
        request.session['user_id'] = result[1].id
        # print "*" * 20
        return redirect("/success")
    else:
        for err in result[1]:
            messages.error(request, err)
        return redirect("/")

def l_process(request):
    # data = {
    # "email": request.POST['email'],
    # "pass": request.POST['pass'],
    # }
    result = User.objects.l_process(data)

    if result[0]:
        request.session['user_id'] =result[1].id
        return redirect("/success")
    else:
        for err in result[1]:
            messages.error(request, err)
        return redirect("/")

def success(request):
    user_obj = User.objects.get(id=request.session['user_id'])
    context = {
    "user" : user_obj
    }
    return render(request, "lr_templates/success.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")
