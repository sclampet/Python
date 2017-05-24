from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(req):
	title = 'Courses'
	courses = Course.objects.all()
	print courses
	context = {
		'title': title,
		'courses': courses
	}
	return render(req, 'courses/index.html', context)

def process(req):
	Course.objects.create(name=req.POST['name'], description=req.POST['description'])
	return redirect('/')

def removecourse(req, id):
	context = {
		'title': 'Remove Course',
		'course': Course.objects.get(id=id)
	}
	return render(req, 'courses/remove.html', context)

def removethis(req, id):
	this = Course.objects.get(id=id)
	this.delete()
	return redirect('/')