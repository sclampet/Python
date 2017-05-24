from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new', views.new, name='new'),
	url(r'^create', views.create, name='create'),
	url(r'^books/(?P<book_id>\d+)$', views.show, name='show'),
	url(r'^books', views.books, name='books'),
	url(r'^destroy/(?P<review_id>\d+)$', views.destroy, name='destroy')
]