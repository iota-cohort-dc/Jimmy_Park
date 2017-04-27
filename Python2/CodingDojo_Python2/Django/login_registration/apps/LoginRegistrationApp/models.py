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
        # checking first name ------------------------------------------>
        if len(data['fname']) < 2:
            flag = False
            errs.append('First Name must contain more than 2 characters')
        if not data['fname'].isalpha():
            flag = False
            errs.append('First Name must not contain numbers')
        if not data['fname']:
            flag = False
            errs.append('Cannot leave First Name field blank')
        # checking last name ------------------------------------------->
        if len(data['lname']) < 2:
            flag = False
            errs.append('Last Name must contain more than 2 characters')
        if not data['lname'].isalpha():
            flag = False
            errs.append('Last Name must not contain numbers')
        if not data['lname']:
            flag = False
            errs.append('Cannot leave Last Name field blank')
        # checking email
        if not EMAIL_REGEX.match(data['email']):
            flag = False
            errs.append("This is an invalid email")
        if not data['email']:
            flag = True
            errs.append("Email field cannot be blank")
        # checking password ------------------------------------------->
        if data['pass'] != data['cpass']:
            flag = False
            errs.append("Your passwords do not match")
        # all is validated, now encrypt ------------------------------->
        if flag:
            hashed = bcrypt.hashpw(data['pass'].encode(), bcrypt.gensalt())
            #<---------------- above has .encode()------------------->
            user = User.objects.create(first_name = data['fname'],last_name = data['lname'], email = data['email'], password = hashed)
            # flash("You are Registered! Please Login!")
            print hashed
            return (True, user)
        else:
            return (False,errs)

    def login(self,data):
        flag = True
        errs = []

        user_in_question = User.objects.filter(email=data['email'])
        # above, pulling from data base and setting to user_in_question

        if user_in_question:
            hashed = User.objects.get(email = data['email']).password
            password = data['pass'].encode('utf-8')

            if bcrypt.hashpw(str(password), str(hashed)):
                # password comes from the form in login, it needs to be inside str()
                # hashed comes from the db, it also needs to be inside str()
                flag = True
            else:
                passFlag = False
                errs.append("Unsuccessful login. Incorrect Password")
        else:
            passFlag = False
            errs.append("Unsuccessful login. Your email is incorrect")

        print user_in_question
        return (True, user_in_question[0])

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    #object UserManager is created and inherits attributes of User
