from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.auth_page, name='auth_page'),
    url(r'^register/', views.register_page, name='register_page'),
]
