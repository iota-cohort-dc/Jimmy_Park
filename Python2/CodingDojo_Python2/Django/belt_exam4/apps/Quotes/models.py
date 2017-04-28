from __future__ import unicode_literals
from django.db import models
from ..LoginReg.models import User


# Create your models here.
class QuoteManager(models.Manager):
    def addNewQuote(self, data, user_id):
        flag = True
        errs = []

        if len(data['quote_by']) < 2:
            flag = False
            errs.append("Quote By field needs to have more than 2 characters.")
        if len(data['quote_message']) < 2:
            flag = False
            errs.append("Quote Message field needs to have more than 2 characters.")
        if data['quote_by'] == "":
            flag = False
            errs.append("Quote By field cannot be blank.")
        if data['quote_message'] == "":
            flag = False
            errs.append("Quote Message cannot be blank.")
        if flag:
            quoteCreate = self.create(
                quote_by = data['quote_by'],
                quote_message = data['quote_message'],
                user_id = user_id,
            )
            return (True, quoteCreate)
        else:
            return (False, errs)

class Quotes(models.Model):
    user = models.ForeignKey(User, related_name='quote_user')
    quote_by = models.CharField(max_length=255)
    quote_message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

class Favorites(models.Model):
    user = models.ForeignKey(User, related_name='fav')
    quotes = models.ForeignKey(Quotes, related_name='quot')
