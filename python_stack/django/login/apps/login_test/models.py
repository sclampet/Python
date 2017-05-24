from __future__ import unicode_literals
from django.db import models
#Our new manager!
class UserManager(models.Manager):
	def login(self, email, password):
		print "Running a login function!"
		print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
		print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
		return 'I will be a future login method made by me!!'
	def register(self, **kwargs):
		print ("Register a user here")
		print ("If successful, maybe return {'theuser':user} where user is a user object?")
		print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
		pass
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	userManager = UserManager()
