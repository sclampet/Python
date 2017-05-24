from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.process),
    url(r'^removecourse/(?P<id>\d+)$', views.removecourse),
    url(r'^removethis/(?P<id>\d+)$', views.removethis)
]