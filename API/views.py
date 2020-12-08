from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class TestView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        content = {'message':'Hello Waleed'}
        return Response(content)