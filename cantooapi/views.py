from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, TagIdNameSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView
from .models import Tag

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class TagList(ListCreateAPIView):
    # Retrieve, update, or delete a tag suggestion
    queryset = Tag.objects.all()
    serializer_class = TagIdNameSerializer
