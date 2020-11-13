from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = BookSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = ReviewSerializer


class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = RatingsSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = MessagesSerializer