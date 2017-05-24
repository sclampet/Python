from django.conf.urls import url
from . import views

app_name = 'user_management'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^users$', views.create, name='create'),
	url(r'^(?P<user_id>\d+)$', views.show, name='show'),
	url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),
]