from __future__ import unicode_literals
from django.db import models
from ..loginReg.models import User


class Books(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

class Authors(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    books = models.ManyToManyField(Books, related_name="authors")

class Reviews(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name="posted_reviews")
    book = models.ForeignKey(Books, related_name="book_reviews")

    #class User(models.Model):
	# name = models.CharField(max_length = 30)
	# username = models.CharField(max_length = 30)
	# email = models.EmailField()
	# password = models.CharField(max_length=100)
	# created_at = models.DateTimeField(auto_now_add = True)
	# updated_at = models.DateTimeField(auto_now = True)
