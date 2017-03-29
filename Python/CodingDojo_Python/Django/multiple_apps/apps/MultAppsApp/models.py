from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re

from django.conf import settings

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, data):
        flag = True
        errs = []

        if len(data['first_name']) < 2:
            flag = False
            errs.append("First cannot be less than 2 characters.")

        if not data['first_name'].isalpha():
            flag = False
            errs.append("First name must not contain numbers.")

        if len(data['last_name']) < 2:
            flag = False
            errs.append("Last cannot be less than 2 characters.")

        if not data['last_name'].isalpha():
            flag = False
            errs.append("Last name must not contain numbers")

        if not EMAIL_REGEX.match(data['email']):
            flag = False
            errs.append("This is an invalid email.")

        if data['pass'] != data['c_pass']:
            flag = False
            errs.append("Your passwords do not match.")

        if flag:
            # messages.success(request, "Success! Welcome, " + userInfo['first_name'] + "!")
            hashed = bcrypt.hashpw(data['pass'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name = data['first_name'], last_name = data['last_name'], email = data['email'], password = hashed)
            # print data
            return (True, user)

        else:
            return(False, errs)

    def l_process(self,data):
        flag = True
        errs = []
        suspect_user = User.objects.filter(email=data['email'])

        if suspect_user:
            hashed = User.objects.get(email = data['email']).password
            hashed = hashed.encode('utf-8')
            password = data['pass']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                # messages.success(request, "Success! Welcome, " + User.objects.get(email = data['email']).first_name + "!")

                print suspect_user
                flag = True
            else:
                # messages.warning(request, "Unsuccessful login. Incorrect password")
                passFlag = False
                errs.append("Unsuccessful login. Incorrect Password")
        else:
            # messages.warning(request, "Unsuccessful login. Your email is incorrect.")
            passFlag = False
            errs.append("Unsuccessful login. Your email is incorrect.")

        print suspect_user
        return (True, suspect_user[0])

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager() #object UserManager is created and inherits attributes of User

# class CoursesApp(models.Models):
#     coursesapp = models.ManyToManyField(User)
