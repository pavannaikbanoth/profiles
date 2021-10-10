from django.shortcuts import render
from rest_framework.response import Response
from.models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets

class Profileviewset(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer