from __future__ import unicode_literals
from django.db import models

# Create your models here.
# class InterestManager(models.Manager):
#     def addInterest(self,data): #user_id
#         print "*" *10, data,"*" *10
#         flag = True
#         errs =[]
#
#         if len(data['name']) < 1:
#             flag = False
#             errs.append("Name cannot be blank")
#         if len(data['interest']) < 1:
#             flag = False
#             errs.append("Interests cannot be blank")
#         if flag:
#             # print "*" * 20, newInterest, "*" * 20
#             # print "*" * 20, newUser, "*" * 20
#             # newInterestUser = self.create(
#             #     interest = interest.objects.find(data['interest'],
#             #     name = data['name'],
#             #     )
#             # newUser = Users.objects.create(name=data['name'])
#             return (True, newInterestUser)
#         else:
#             return (False, errs)

class Interests(models.Model):
    interest = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add='True')
    updated_at = models.DateTimeField(auto_now='True')
    # objects = InterestManager()


# class Users(models.Model):
#     name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add='True')
#     updated_at = models.DateTimeField(auto_now='True')



    # userInterest = models.ManyToManyField(Interests, related_name='user_interest')
    # interest = models.ForeignKey(Interests)

class UsersInterest(models.Model):
    user = models.ForeignKey(Users, related_name='userFK')
    interest = models.ForeignKey(Interests, related_name='interestFK')
