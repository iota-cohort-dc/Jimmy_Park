from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime

def index(request):

    return render(request, ('index.html'))
