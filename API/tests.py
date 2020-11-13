from customer.models import Customer, CustomerStatus
from customer.views import CustomerPartialView
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import pprint
from django.utils import timezone

class UserTest(APITestCase) :

    def user(self) :

    	data = {"name":"john", "email": "john@gmail.com", "password":"12345a", "surname":"doe"}
    	response: self.client.get("api/serializer/User", data)
    	self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookTest(APITestCase) :

    def book(self) :

    	data = {"user":"john", "content": "dostoyevsky", "date":"10.10.2020"}
    	response: self.client.get("api/serializer/Book", data)
    	self.assertEqual(response.status_code, status.HTTP_200_OK)

class CommentTest(APITestCase) :

    def comment(self) :

    	data = {"user":"john", "content": "good", "date":"10.10.2020"}
    	response: self.client.get("api/serializer/Comment", data)
    	self.assertEqual(response.status_code, status.HTTP_200_OK)

class ReviewTest(APITestCase) :

    def review(self) :

    	data = {"user":"john", "book": "crime and punishment", "date":"10.10.2020"}
    	response: self.client.get("api/serializer/Review", data)
    	self.assertEqual(response.status_code, status.HTTP_200_OK)

class RatingsTest(APITestCase) :

    def ratings(self) :

    	data = {"user":"john", "rate": "5", "book":"don quixote"}
    	response: self.client.get("api/serializer/Ratings", data)
    	self.assertEqual(response.status_code, status.HTTP_200_OK)

class MessagesTest(APITestCase) :

    def messages(self) :

    	data = {"user_from":"john", "user_to": "nicolas", "message":"hello", "created_at":"10.10.2020"}
    	response: self.client.get("api/serializer/Message", data)
    	self.assertEqual(response.status_code, status.HTTP_200_OK)