from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from datetime import datetime as dt

from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model

from .models import Book
from . serializer import UserProfileSerializer, RegisterSerializer, BookSerializer

from . import views
from .api import RegisterAPI
import json
# Create your tests here.


class GetAllUserTest(TestCase):
    def test_get_all_users(self):
        response = self.client.get(reverse(views.users_list))
        users = User.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllBooksTest(TestCase):
    def test_get_all_books(self):
        response = self.client.get(reverse(views.book_list))
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestSingleValidBook(TestCase):
    def test_get_single_book(self):
        book = Book.objects.first()
        if book:
            response = self.client.get(reverse('book_details', args=book.id))
            print("response => ", response)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertIsNone(book)


class TestRegisteration(TestCase):
    def setUp(self):
        self.validated_data = {
        "first_name": "Waleed",
        "last_name": "Saleh",
        "username": "waalfededvtest",
        "email": "walefcded@tesddt.com",
        "password": "111111",
        "confirm_password": "111111"
    }

    def test_create_valid_user(self):
        response = self.client.post(reverse("register"), data=json.dumps(self.validated_data), 
                                content_type='application/json')
   
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
