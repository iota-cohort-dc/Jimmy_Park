from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from ..LoginReg.models import User
from .models import Product
from django.core.urlresolvers import reverse
from django.db.models import Q
import datetime
from time import gmtime, strftime

def index(request):
    context = {  # Q and | allow me to do compare two columns
	'my_wish': Product.objects.filter(Q(planned_user_id=request.session['user_id']) | Q(joining_user =request.session['user_id'])),
	# for the user who's logged in:  -- I planned the trip ((or)) I joined the trip --
	'not_mine': Product.objects.all().exclude(Q(planned_user_id=request.session['user_id']) | Q(joining_user =request.session['user_id'])),
	# for the user who's logged in:  -- I DIDN'T plan the trip ((or)) I DIDN'T join the trip --
	'users': User.objects.get(id=request.session['user_id'])
	}
    return render(request,"WishList/index.html", context)

def addProductPage(request):
    return render(request,"WishList/addProductPage.html")

def addProduct(request):
    result = Product.objects.addNewProduct(request.POST, request.session['user_id'])
    if result[0]:
        print"*"*50
        print result
        return redirect(reverse("wishList:index"))
    else:
        for errs in result[1]:
			# messages.error(request, errs)
            return redirect(reverse("wishList:addProductPage"))
    return redirect(reverse("wishList:index"))

def joinWish(request,id):
	joining = User.objects.get(id=request.session['user_id'])
	product_joining = Product.objects.get(id=id)
	product_joining.joining_user.add(joining)
	return redirect(reverse('wishList:index'))

def showProduct(request,id):
	context = {
		'products': Product.objects.get(id = id),
	}

	return render(request,"WishList/product_page.html", context)

def delete(request, id): #item_id
    Product.objects.get(id=item_id).delete()
    return redirect(reverse('wishList:index'))

def remove(request, id): #item_id
    user = User.objects.get(id=request.session['user_id'])
    item = Product.objects.get(id=id)
    item.joining_user.remove(user)
    return redirect(reverse('wishList:index'))
