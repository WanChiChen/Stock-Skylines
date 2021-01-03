from django.shortcuts import render
from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer


class ListProject(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DetailProject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer