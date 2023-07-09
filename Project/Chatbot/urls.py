from django.contrib import admin
from django.urls import path
from Chatbot import views

urlpatterns = [
    path('', views.index, name='Chatbot'),
    path('index', views.index, name='index'),
    #path('os', views.os, name='os'),
    path('cources', views.cources, name='cources'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout')
   
]