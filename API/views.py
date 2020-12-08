from django.shortcuts import render
from rest_framework.views import APIView,APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from rest_framework import viewsets
from .serializer import BookSerializer, ProfileSerializer, UserProfileSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# Create your views here.



@api_view(['GET'])
def book_list(request):
    books = Book.objects.all().order_by('-name')
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_user(request,pk):
    user = User.objects.get(pk=pk)
    serializer = UserProfileSerializer(user, many=False)
    return Response(serializer.data)





    