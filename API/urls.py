from django.urls import path,include

from . import views
from .api import RegisterAPI
from rest_framework import routers

namesapce = 'api'


urlpatterns = [
    path('hello/', views.TestView.as_view(),name='test'),
    path('register/', RegisterAPI.as_view(),name="register"),
    path('books/',views.book_list,name="books"),
    path('book/<int:pk>/', views.book_details, name="book_details"),
    
]
