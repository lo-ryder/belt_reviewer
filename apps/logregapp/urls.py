from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^$', views.index, name='index'),
]
