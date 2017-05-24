from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
# survey form
def index(request):
	title = "Survey Form"
	location = ['Seattle', 'Denver', 'LA']
	language = ['Python', 'Javascript', 'CSS']
	context = {
		'title': title,
		'locations': location,
		'languages': language
	}
	# print context
	return render(request, 'surveyform/index.html', context)

#result page that shows survey info
def result(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	context = {
		'name': request.session['name'],
		'location': request.session['location'],
		'language': request.session['language'],
		'comment': request.session['comment'],
		'count': request.session['count']
	}
	return render(request, 'surveyform/result.html', context)

# process form
def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')