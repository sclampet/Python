from django.shortcuts import render, redirect
import random
import string


# Create your views here.
def index(request):
	new_word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
	context = {
		'new_word': new_word,
	}
	print new_word
	return render(request, 'randomword/index.html', context)

# def create(request):
# 	if request.method == "POST":
# 		req
