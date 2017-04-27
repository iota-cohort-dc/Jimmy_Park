from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    name = models.ForeignKey(User, related_name='name_name')
    friend = models.ForeignKey(User, related_name='friend_friend')
