from django.urls import path

from . import views
from .api import RegisterAPI

namesapce = 'api'

urlpatterns = [
    path('hello/', views.TestView.as_view(),name='test'),
    path('register/', RegisterAPI.as_view(),name="register")
]
