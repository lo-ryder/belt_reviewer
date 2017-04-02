from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.users, name='users'),
    url(r'^reviews/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^reviews/create$', views.create, name='create'),
]
