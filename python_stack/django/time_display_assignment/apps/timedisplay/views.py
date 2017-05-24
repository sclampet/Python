from django.shortcuts import render

# Create your views here.
def index(request):
	date = {
		'date': 'Jan. 9 2017'
	}
	return render(request, 'timedisplay/index.html', date)