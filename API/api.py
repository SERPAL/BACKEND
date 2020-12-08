from rest_framework import generics, permissions,mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .serializer import RegisterSerializer, UserProfileSerializer
from rest_framework.serializers import ValidationError
import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse
#Register API
#Using generics views
class RegisterAPI(generics.GenericAPIView):
    print("1")
    #Adding the serialized class for registeration
    serializer_class = RegisterSerializer
    print("2")
    #Overriding the method to make our own registeration
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data= request.data)
            serializer.is_valid(raise_exception = True)
            user = serializer.save()
            return Response({
                'user':UserProfileSerializer(user, context = self.get_serializer_context()).data,
                'message': "User Created successfully you can now login",       
                    })
        except Exception as e:
            print("The error is in the post_Register_API => ", e)
            print("Fuul details => ", type(e.get_full_details()))
            return Response({"error": e.get_full_details()})

