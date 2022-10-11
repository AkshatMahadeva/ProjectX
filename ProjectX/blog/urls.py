from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib import messages

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('createPost/', views.createPost, name="createPost"),
]