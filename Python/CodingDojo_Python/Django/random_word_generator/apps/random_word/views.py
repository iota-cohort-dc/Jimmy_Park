from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "index.html")

def generate(request):

    if request.method == 'GET':
        request.session['new_word'] = get_random_string(length=14)
        request.session['count'] += 1
        return redirect( "/")



        # return render(request, "random_word/index.html")
