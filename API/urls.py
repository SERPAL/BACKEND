from django.urls import path,include

from . import views
from .api import RegisterAPI, UpdateUserAPI
from rest_framework import routers

namesapce = 'api'


urlpatterns = [
    path('users/', views.users_list, name="users"),
    path('register/', RegisterAPI.as_view(),name="register"),
    path('books/',views.book_list,name="books"),
    path('book/<int:pk>/', views.book_details, name="book_details"),
    path('edit-user/<int:pk>/', UpdateUserAPI.as_view(), name="edit_user")
]
