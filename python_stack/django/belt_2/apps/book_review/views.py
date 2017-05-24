from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Book, Review



# Create your views here.
def index(req):
	books = Book.objects.pull_recent_books()
	reviews = Review.objects.pull_recent_reviews()
	context = {
		'books': books,
		'reviews': reviews,
	}
	return render(req, 'book_review/index.html', context)

def new(req):
	if not req.session['user_id']:
		return redirect(reverse('user_management:index'))
	context = {
		'authors': Book.objects.order_by('author')
	}
	return render(req, 'book_review/new.html', context)

def create(req):
	if req.method == 'POST':
		valid, res = Review.objects.validate_and_add(req.POST, req.session['user_id'])

		if valid:
			print 'Got new review!!'
			return redirect('book_review:index')
		else:
			for error in res:
				messages.error(req, error)
			return redirect('book_review:new')

	return redirect('book_review:new')

def show(req, book_id):
	valid, res = Book.objects.pull_book_info(book_id)
	if valid:
		context = {
			'book_info': res,
		}
	else:
		for error in res:
			messages.error(req, error)
		return render(req, 'book_review/book_details.html')
	return render(req, 'book_review/book_details.html', context)

def books(req):
	books = Book.objects.all().order_by('-updated_at')
	context = {
		'books':books,
	}
	return render(req, 'book_review/books.html', context)

def destroy(req, review_id):
	if req.method == 'POST':
		user_id = req.session['user_id']
		valid = Review.objects.destroy_review(review_id, user_id)
	return redirect('book_review:index')