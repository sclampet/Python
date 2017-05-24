from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(req):
	return render(req, 'user_management/index.html')

def create(req):
	if req.method == "POST":
		valid, response = User.objects.val_and_add(req.POST)
		if valid:
			req.session['user_id'] = response.id
			req.session['alias'] = response.alias
			return redirect('book_review:index')
		else:
			for error in response:
				messages.error(req, error)
			return redirect('user_management:index')
	else:
		return redirect('user_management:index')

def login(req):
	if req.method == "POST":
		valid, res = User.objects.login_check(req.POST)
		if valid:
			req.session['user_id'] = res.id
			req.session['alias'] = res.alias
			print req.session['alias']
			return redirect('book_review:index')
		else:
			for error in res:
				messages.error(req, error)
	else:
		messages.error(req, "Oops! Something went wrong!")
	return redirect('user_management:index')

	return redirect('user_management:index')

def logout(req):
	req.session.clear()
	return redirect('book_review:index')

def show(req, user_id):
	valid, res = User.objects.get_user_info(user_id)
	print res
	if valid:
		context = {
			'user_info': res,
		}
	else:
		messages.error(req, res)
		return render(req, 'user_management/user_details.html')
	return render(req, 'user_management/user_details.html', context)
