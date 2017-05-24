from __future__ import unicode_literals

from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
	def isValidEmail(self, email):
		if len(email) < 1:
			return False
		elif not EMAIL_REGEX.match(email):
			return False
		else:
			return True


	
class User(models.Model):
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()