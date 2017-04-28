from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Quotes, Favorites
from ..LoginReg.models import User

def index(request):


    context = {
        'quotes': Quotes.objects.all(),
        # 'postedBy': User.objects.all(),
        'user': User.objects.get(id=request.session['user_id']),
        'favorite': Favorites.objects.all(),
    }



    return render(request,"Quotes/index.html", context)

def addQuote(request):

    result = Quotes.objects.addNewQuote(request.POST, request.session['user_id'])

    if result[0]:
        return redirect(reverse("quotes:qindex"))

    else:
        for errs in result[1]:
            message.error(request, errs)

        return redirect("/")

def addFavorite(request): # need to pass in ,id

    # addToFav = User.objects.get(id=request.session['user_id'])
    # addingFavQuote = Quotes.objects.get(id=id)
    # the line above giving error: int() argument must be a string or a number, not 'builtin_function_or_method'

    # Favorites.addingFavQuote.add(addToFav)
    # addingFavQuote.user_id.add(addToFav)

    return render(request,"Quotes/index.html")
    # return redirect(reverse("quotes:qindex"))
