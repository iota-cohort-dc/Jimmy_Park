from __future__ import unicode_literals
from django.db import models # from ..BeltReviewApps.models import User
from django.contrib import messages
import bcrypt
import re
from django.conf import settings
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager): #
    def validate(self,data):
        flag = True
        errs = []
        # checking first name
        if len(data['first_name']) < 2:
            flag = False
            errs.append('First Name must contain more than 2 characters')
        if not data['first_name'].isalpha():
            flag = False
            errs.append('First Name must not contain numbers')
        if not data['first_name']:
            flag = False
            errs.append('Cannot leave First Name field blank')
        # checking last name
        if len(data['last_name']) < 2:
            flag = False
            errs.append('Last Name must contain more than 2 characters')
        if not data['last_name'].isalph():
            flag = False
            errs.append('Last Name must not contain numbers')
        if not data['last_name']:
            flag = False
            errs.append('Cannot leave Last Name field blank')
        # checking email
        if not EMAIL_REGEX.match(data['email']):
            flag = False
            errs.append("This is an invalid email")
        if not data['email']:
            flag = True
            errs ########left off herereeerereererererererererere
        # checking password
        if data['pass'] != data['cpass']:
            flag = False
            errs.append("Your passwords do not match")
        # all is validated, now encrypt
        if flag:


    def login

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
