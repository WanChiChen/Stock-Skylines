from django.shortcuts import render
from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

@api_view(['POST'])
def stock_detail(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data = data)

        if serializer.is_valid():
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 