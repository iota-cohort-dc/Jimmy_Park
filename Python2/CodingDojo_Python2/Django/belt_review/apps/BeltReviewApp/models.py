
from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validate(self, data):
		flag = True
		errors = []
		if len(data['name']) < 3:
			flag = False
			errors.append('Name must be greater than 3 characters')
		if len(data['user_name']) < 3:
			flag = False
			errors.append('Username must be greater than 3 characters')
		if not EMAIL_REGEX.match(data['email']):
			flag = False
			errors.append('Email must be valid format')
		if len(data['password']) < 8:
			flag = False
			errors.append('Password must be at least 8 characters in length')
		if data['passconfirm'] != data['password']:
			flag = False
			errors.append('Confirm Password must match Password')

		if flag:
			passverd = data['password']
			hashed = bcrypt.hashpw(str(passverd), bcrypt.gensalt())
			user = User.objects.create(name=data['name'], username=data['user_name'],email=data['email'] ,password=hashed)
			return (True, user)
		else:
			return (False, errors)

class User(models.Model):
	name = models.CharField(max_length = 30)
	username = models.CharField(max_length = 30)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()
