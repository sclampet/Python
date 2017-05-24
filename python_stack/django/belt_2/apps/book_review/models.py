from __future__ import unicode_literals

from django.db import models
from ..user_management.models import User

# Create your models here.
class BookManager(models.Manager):
	def create_book(self, title, author):
		book = self.create(title=title, author=author)
		print "creating book...."
		return book

	def pull_recent_books(self):
		books = self.all().order_by('-updated_at')[:5]
		return books

	def pull_book_info(self, book_id):
		book_id = int(book_id)
		try:
			book = self.get(id=book_id)
			print "got the book!"
			#initialize return object
			response = {
				'author': book.author,
				'title': book.title,
				'book_id': book.id,
				'reviews': Review.objects.filter(review_book=book).order_by('-created_at'),
			}
			return (True, response)
		except:
			error = "Something went wrong!"
			return (False, error)


class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BookManager()	

class ReviewManager(models.Manager):
	def create_review(self, review, rating, book, user):
		print "creating review..."
		review = self.create(review=review, rating=rating, review_book=book, review_user=user)
		return review

	def pull_recent_reviews(self):
		reviews = self.all().order_by('-updated_at')[:3]
		return reviews

	def validate_and_add(self, data, user_id):
		#upack data
		title = data['title']
		author_select = data['author-select']
		author_text = data['author-text']
		author = ''
		review = data['review']
		rating = int(data['rating'])
		#errors handler
		errors = []

		#execute validations
		if len(title) < 1:
			errors.append('Please enter a title for your book.')
		if author_select:
			author = author_select
		elif author_text:
			author = author_text
		elif not author_select or not author_text:
			errors.append('Please enter an author for your book.')
		if len(review) < 1:
			errors.append('Please leave a review.')

		#break as soon as there are errors
		if errors:
			return (False, errors)

		try:
			user = User.objects.get(id=user_id)
			book = Book.objects.create_book(title, author)
			review = self.create_review(review, rating, book, user)
			return (True, review)
		except:
			errors.append('Oh no, you might now be logged in!')
			return (False, errors)

	def destroy_review(self, review_id, user_id):
		review_id = int(review_id)
		user_id = int(user_id)
		try:
			review = self.get(id=review_id)
			user = User.objects.get(id=user_id)
			if user != review.review_user:
				return False
			else:
				review.delete()
				return True
		except:
			return False

class Review(models.Model):
	review = models.TextField(max_length=5000)
	rating = models.SmallIntegerField()
	review_book = models.ForeignKey(Book, related_name='book_review')
	review_user = models.ForeignKey(User, related_name='user_review')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReviewManager()
