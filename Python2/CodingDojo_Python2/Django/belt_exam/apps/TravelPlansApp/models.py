from __future__ import unicode_literals
from django.db import models
from ..TravelBuddyApp.models import User
import datetime


class TripsManager(models.Manager):
    def addNewTrip(self,data,user_id):
        flag = True
        errs = []

        if len(data['destination']) < 1:
            flag = False
            errs.append("Destination cannot be blank")

        if len(data['description']) < 1:
            flag = False
            errs.append("Description cannot be blank")

        if data['travelStart'] < str(datetime.date.today()):
            flag = False
            print "222222" * 30
            print str(datetime.date.today())
            print data['travelStart']
            errs.append("Start cannot be before todays date")
            # return (False, errs)

        if data['travelStart'] == "":
            flag = False
            errs.append("Cannot leave blank")

        if data['travelEnd'] < data['travelStart']:
            flag = False
            errs.append('Cannot have end date before start date')
            # return (False, errs)

        if data['travelEnd'] == "":
            flag = False
            errs.append("Cannot leave blank")


        if flag:
            # print "444444" * 15
            # print "AW" * 30
            self.create(
            destination = data['destination'],
            travelStart = data['travelStart'],
            travelEnd = data['travelEnd'],
            description = data['description'],
            planned_user_id = user_id,
            )
            return (True)

class Trips(models.Model):
    destination = models.CharField(max_length=255)
    travelStart = models.DateField()
    travelEnd = models.DateField()
    description = models.TextField(max_length=500)
    joining_user = models.ManyToManyField(User, related_name='joiningtrip')
    planned_user = models.ForeignKey(User, related_name='plannertrip')
    objects = TripsManager()
