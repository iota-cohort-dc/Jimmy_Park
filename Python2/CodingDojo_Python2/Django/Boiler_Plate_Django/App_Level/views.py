from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Books, Authors, Reviews, User # this is example

from .models import User
from django.core.urlresolvers import reverse
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
