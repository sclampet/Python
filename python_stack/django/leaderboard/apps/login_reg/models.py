from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# Create your models here.
class Manager(models.Manager):
	def validRegistration(self, userInfo):
		#registration form validations
		errors = []
		if not userInfo['first_name'].isalpha():
			errors.append('First name must only contain letters!')
		if len(userInfo['first_name']) < 1:
			errors.append('Please put a first name!')

		if not userInfo['last_name'].isalpha():
			errors.append('Last name must only contain letters!')
		if len(userInfo['last_name']) < 1:
			errors.append('Please put a last name!')

		if not EMAIL_REGEX.match(userInfo['email']):
			errors.append('Must be a valid email!')
		if len(userInfo['email']) < 1:
			errors.append('Please put a valid email!')
		if User.objects.filter(email=userInfo['email']):
			errors.append('A user with that email already exists!')

		if len(userInfo['password']) < 8:
			errors.append('Password must be at least 8 characters long!')
		if userInfo['password'] != userInfo['confirm']:
			errors.append('Passwords do not match!')

		if errors:
			return (False, errors)
		else:
			errors.append('Great! Thanks for registering '+userInfo['first_name']+'!')
			hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(first_name=userInfo['first_name'], last_name=userInfo['last_name'], email=userInfo['email'], pw_hash=hashed)
			return (True, user)

	def userExistsLogin(self, userInfo):
		#check to see if user already exists
		errors = []
		if len(userInfo['email']) < 1 or len(userInfo['password']) < 1:
			errors.append('Please fill in both an email and password!')
		elif not EMAIL_REGEX.match(userInfo['email']):
			errors.append('Make sure you have a valid email!')
		else:
			if User.objects.filter(email=userInfo['email']):
				hashed = User.objects.get(email=userInfo['email']).pw_hash.encode()
				password = userInfo['password'].encode()
				if bcrypt.hashpw(password, hashed) == hashed:
					errors.append('Success! Welcome, '+User.objects.get(email=userInfo['email']).first_name+'!')
				else:
					errors.append('Invalid password!')
			else:
				errors.append('Invalid Email!')

		if errors:
			return (False, errors)
		else:
			return (True, errors)
		



class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=100)
	pw_hash = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = Manager()