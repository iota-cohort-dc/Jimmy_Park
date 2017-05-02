from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Quotes
from ..LoginReg.models import User
from django.db.models import Q
from django.db.models import Count

def index(request):
    context = {
        'quotes': Quotes.objects.all().exclude(favorited_by=request.session['user_id']),
        'user': User.objects.get(id=request.session['user_id']),
        'inMyFav': Quotes.objects.filter(favorited_by=request.session['user_id']),
        # 'logUser': Quotes.objects.filter(id=logged_in_user_id),

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

def addFavorite(request,id): # need to pass in ,id
    addFavToUser = User.objects.get(id=request.session['user_id'])
    # create var addFavToUser to person who's logged in
    addFavQuoteContent = Quotes.objects.get(id=id)
    # create var addFavQuoteContent to quote_id
    addFavQuoteContent.favorited_by.add(addFavToUser)
    # join addFavQuoteContent -- ManyToManyField(favorited_by) and .add addFavToUser
    return redirect(reverse("quotes:qindex"))

def removeFavorite(request,id):  #id comes from link tag, gets passed in here
    removeFavToUser = User.objects.get(id=request.session['user_id'])
    # create var removeFavToUser to person who's logged in
    removeFavQuoteContent = Quotes.objects.get(id=id)
    # create var removeFavQuoteContent to the quote_id
    removeFavQuoteContent.favorited_by.remove(removeFavToUser)
    return redirect(reverse("quotes:qindex"))

def userInfoPage(request,id): #id comes from link tag, gets passed in here
    data = {
        'all_quotes': Quotes.objects.filter(logged_in_user_id=id),
        'count': User.objects.filter(id=id).annotate(num_quotes=Count('quote_user')),
        'name': User.objects.get(id=id),
        # id comes from the link tag that has id, gets passed in here.

    }
    return render(request,"Quotes/users.html", data)
