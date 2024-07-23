from django.contrib import admin
from django.urls import path

from resto import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('aboutus/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('form/', views.form, name='form')
]
