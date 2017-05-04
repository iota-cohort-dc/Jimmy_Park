from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    notes = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Projects(models.Model):
    pro_name = models.CharField(max_length=255)
    pro_notes = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Clients, related_name='clientFK')
