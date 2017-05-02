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

    # notSureFavorites = Quotes.objects.filter(id=request.session['user_id'], quote_by = Quote.)


    return render(request,"Quotes/index.html", context)

def addQuote(request):

    result = Quotes.objects.addNewQuote(request.POST, request.session['user_id'])

    if result[0]:
        return redirect(reverse("quotes:qindex"))

    else:
        for errs in result[1]:
            message.error(request, errs)

        return redirect("/")

def addFavorite(request,id): # need to pass in ,id
# <----------------below was in here previously --------->
    addToFav = User.objects.get(id=request.session['user_id'])
    addingFavQuote = Quotes.objects.get(id=id)

    # Favorites.objects.create(quotes=addingFavQuote,user=addToFav) this need if..
    # the line above giving error: int() argument must be a string or a number, not 'builtin_function_or_method'

    # Favorites.addingFavQuote.add(addToFav)
    # addingFavQuote.user_id.add(addToFav)
# <-------------above was in here previously------------>

# <-----------------below does not work---------------->
# -------have repeating keywords-------
    # quotes = Quotes.objects.get(id=id)
    # user = User.objects.get(id=request.session['user_id'])
    # check = Favorites.objects.filter(user = user).filter(quotes = quotes)
    # if not check:
    #     Favorites.objects.filter(quotes=quotes, quotes=user)
    # else:
    #     messages.error(request,"This is already one of your favorites")
    # return redirct(reverse("quotes:index"))
    # <--------------above does not work--------------->
    # ----have repeating keywords---------




    return render(request,"Quotes/index.html")
    # return redirect(reverse("quotes:qindex"))
