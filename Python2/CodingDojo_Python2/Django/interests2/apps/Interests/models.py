from __future__ import unicode_literals
from django.db import models

# Create your models here.
class InterestManager(models.Manager):
    def addInterest(self,data): #user_id
        print data
        flag = True
        errs =[]

        if len(data['name']) < 1:
            flag = False
            errs.append("Name cannot be blank")
        if len(data['interest']) < 1:
            flag = False
            errs.append("Interests cannot be blank")
        if flag:
            newInterest = self.create(
                interest = data['interest'],
                # interest_id = user_id,
            )
            print newInterest
            newUser = User.create(name=data['name'], interest = newInterest)
            return (True, newInterest)
        else:
            return (False, errs)



class Interests(models.Model):
    interest = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add='True')
    updated_at = models.DateTimeField(auto_now='True')
    objects = InterestManager()
class Users(models.Model):
    name = models.CharField(max_length=50)
    interest = models.ForeignKey(Interests)
    created_at = models.DateTimeField(auto_now_add='True')
    updated_at = models.DateTimeField(auto_now='True')
