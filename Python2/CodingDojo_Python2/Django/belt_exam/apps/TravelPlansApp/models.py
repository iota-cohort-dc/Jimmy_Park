from __future__ import unicode_literals
from django.db import models
from ..TravelBuddyApp.models import User


class Trips(models.Model):
    destination = models.CharField(max_length=255)
    travelStart = models.DateField(blank=True, null=True, verbose_name='date')
    travelEnd = models.DateField(blank=True, null=True, verbose_name='date')
    description = models.TextField(max_length=500)
    user = models.ManyToManyField(User, related_name='trips')
