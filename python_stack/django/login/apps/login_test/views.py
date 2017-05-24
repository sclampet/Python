from django.shortcuts import render, HttpResponse
from .models import User
# Create your views here.
def index(request):
	User.userManager.login('scott@viewzr.com', 'password')
	return HttpResponse(User.userManager.login('scott@viewzr.com', 'password'))