from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^add/author$', views.newauthor, name='newauthor'),
    url(r'^add$', views.newbook, name='newbook'),
    url(r'^(?P<id>\d+)$', views.info, name='info'),
    url(r'^$', views.home, name='home'),
]
