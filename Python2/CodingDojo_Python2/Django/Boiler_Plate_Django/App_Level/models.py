from __future__ import unicode_literals
from django.db import models
from ..BeltReviewApps.models import User

##<-------------------------------------------------------------------
login reg
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re
from django.conf import settings
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
##<-------------------------------------------------------------------

# create this / try writing on paper first then apply
# class name is NOUN
# this is like the ERD from MySQL
class Books(models.Model):
    title = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)

class Authors(models.Model):
    name = models.CharField(max_length = 255)
    books = models.ManyToManyField(Books, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    comments = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    ratings = models.IntegerField()
    book = models.ForeignKey(Books, related_name="book_reviews")
    user = models.ForeignKey(User, related_name="posted_reviews")
