from __future__ import unicode_literals
from django.db import models
from ..MultAppsApp.models import User

class Courses(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class LoginReg(models.Model):
    user = models.ForeignKey(User, related_name="all_users")
    course = models.ForeignKey(Courses, related_name="all_courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
