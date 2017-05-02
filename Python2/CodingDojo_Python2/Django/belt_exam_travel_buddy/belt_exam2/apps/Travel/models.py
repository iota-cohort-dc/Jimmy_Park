from __future__ import unicode_literals
from django.db import models
from ..LoginReg.models import User
import datetime # for using

#<----------------- Travel ----------------->

class TravelsManager(models.Manager):
    def validate(self, data, user_id):
        flag = True
        errs = []

        if len(data['destination']) < 1:
            flag = False
            errs.append('Destination cannot be blank!')
        if len(data['description']) < 1:
            flag = False
            errs.append('Description cannot be blank')
        if data['departure'] < str(datetime.date.today()):
            flag = False
            errs.append('Departure date cannot be before todays date')
        if data['departure'] == "":
            flag = False
            errs.append('Departure cannot be blank')
        if data['arrival'] < data['departure']:
            flag = False
            errs.append('Arrival cannot be before departures date')
        if data['arrival'] == "":
            flag = False
            errs.append('Arrival cannot be blank')

        if flag: # will write into the database.
            validatepassed = self.create(
                destination = data['destination'],
                description = data['description'],
                departure = data['departure'],
                arrival = data['arrival'],
                userplanning_id = user_id,
            )
            return (True, validatepassed)
            # True and validatepassed gets passed to views.
        else:
            return (False, errs)

class Travels(models.Model):
    destination = models.CharField(max_length=255)
    departure = models.DateField()
    arrival = models.DateField()
    description = models.CharField(max_length=255)
    userjoining = models.ManyToManyField(User, related_name='user_joining')
    userplanning = models.ForeignKey(User, related_name='user_planning')
    objects = TravelsManager()
