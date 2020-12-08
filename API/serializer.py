from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db import models
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
        'username', 'email','password', "confirm_password")
        extra_kwargs = {
            'password':{'write_only': True},
            'confirm_password':{'write_only': True}
        }

    def validate_password(self, value):
        data = self.get_initial()
        confirm_password = data.pop('confirm_password')
        print("In the validation!")
        password = data.get('password')
        print("password => ", password)
        print("confirm_passowrd => ", confirm_password)
        if password != confirm_password:
            print("First error")
            raise serializers.ValidationError('Passwords must match')
        if password is None and confirm_password is None:
            print("Second error")
            raise serializers.ValidationError('Passwords are not filled')
        else:
            print("No error")
            return value
        

    def create(self,validated_data):
        try:
            password = validated_data['password']
            user = User.objects.create(username = validated_data['username'], 
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],email=validated_data['email'])
            user.set_password(password)
            user.save()
            profile = Profile.objects.create(user=user)
            return user
        except Exception as e:
            print("The error is in Register Serilazer create =>", e)
            return Response({"error": {{k:v} for k,v in e.items()}})
