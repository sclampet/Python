from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	context = {
		'title': 'Login and Registration'
	}
	return render(request, 'login_reg/index.html', context)

def login(request):
	if request.method == 'POST':
		# print request.POST
		valid, response = User.objects.userExistsLogin(request.POST)
		# print valid
		# print response
		if not valid:
			for error in response:
				# print error
				messages.error(request, error)
				return redirect('login:index')
		else:
			return redirect('ninjagold:index')
	else:
		return redirect('login:index')

def register(request):
	if request.method == 'POST':

		valid, response = User.objects.validRegistration(request.POST)

		if not valid:
			for error in response:
				messages.error(request, error)
			return redirect('login:index')
		else:
			return redirect('leaderboard:index')
	else:
		return redirect('login:index')