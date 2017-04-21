from __future__ import unicode_literals
from django.db import models
from ..LoginRegApp.models import User

class Books(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Authors(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Books, related_name="authors")

class Reviews(models.Model):
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='posted_reviews')
    book = models.ForeignKey(Books, related_name='book_reviews')















    # create this / try writing on paper first then apply
    # class name is NOUN
    # this is like the ERD from MySQL
