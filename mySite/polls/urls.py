from django.urls import path 
from . import views

urlpatterns = [
    path('hello', views.index, name='index'),
    path('shubham', views.contact, name='Shubham'),
    path('template', views.template, name='template'),
    path('about', views.templateabout, name='about')
]