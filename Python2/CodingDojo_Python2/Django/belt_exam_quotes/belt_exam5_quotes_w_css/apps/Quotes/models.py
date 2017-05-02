from __future__ import unicode_literals
from django.db import models
from ..LoginReg.models import User

class QuoteManager(models.Manager):
    def addNewQuote(self, data, user_id):
        flag = True
        errs = []

        if len(data['author_of_quote']) < 2:
            flag = False
            errs.append("Quote By field needs to have more than 2 characters.")
        if len(data['quote_content']) < 2:
            flag = False
            errs.append("Quote Message field needs to have more than 2 characters.")
        if data['author_of_quote'] == "":
            flag = False
            errs.append("Quote By field cannot be blank.")
        if data['quote_content'] == "":
            flag = False
            errs.append("Quote Message cannot be blank.")
        if flag:
            quoteCreate = self.create(
                author_of_quote = data['author_of_quote'],
                quote_content = data['quote_content'],
                logged_in_user_id = user_id,
            )
            return (True, quoteCreate)
        else:
            return (False, errs)

# class User(models.Model): ((*** from LoginReg ***))
#     name = models.CharField(max_length=45)
#     alias = models.CharField(max_length=45)
#     email = models.EmailField(max_length=45)
#     birth_date = models.DateField()
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Quotes(models.Model):
    logged_in_user = models.ForeignKey(User, related_name='quote_user')
    author_of_quote = models.CharField(max_length=255)
    quote_content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorited_by = models.ManyToManyField(User, related_name='favorited_by_user')
    objects = QuoteManager()



# above is many to many
# below is one to many
# class Favorites(models.Model):
#     user_fav_quote = models.ForeignKey(User, related_name='user_fav_quote')
#     fquote_q = models.ForeignKey(Quotes, related_name='fquot_q')
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
