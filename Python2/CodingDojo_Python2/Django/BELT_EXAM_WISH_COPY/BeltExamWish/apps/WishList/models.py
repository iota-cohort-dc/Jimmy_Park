from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib import messages
import datetime
from ..LoginReg.models import User

class ProductManager(models.Manager):
    def addNewProduct(self, data, user_id):
        flag = True
        errs = []

        if len(data['product']) < 2:
            flag = False
            errs.append("product By field needs to have more than 2 characters.")

        if data['product'] == "":
            flag = False
            errs.append("product By field cannot be blank.")

        if flag:
            productCreate = self.create(
                product = data['product'],
                planned_user_id = user_id,
            )
            return (True, productCreate)
        else:
            return (False, errs)

class Product(models.Model):
    product = models.CharField(max_length=255)
    planned_user = models.ForeignKey(User, related_name='plannertrip')
    joining_user = models.ManyToManyField(User, related_name='joiningtrip')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
