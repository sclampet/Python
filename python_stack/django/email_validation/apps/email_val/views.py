from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(req):
	context = {
		'title': 'Email Validation'
	}
	return render(req, 'email_val/index.html', context)

def submit(req):
	if req.method == 'POST':
		email = req.POST['email']
		if User.objects.isValidEmail(email):
			User.objects.create(email=email)
			messages.success(req, email + ' is a valid email!')
			return redirect('/success')
		else:
			messages.warning(req, 'Invalid Email!')
			return redirect('/')
	else:
		return redirect('/')


def success(req):
	context = {
		'title': 'Current Emails',
		'emails': User.objects.all()
	}

	return render(req, 'email_val/success.html', context)