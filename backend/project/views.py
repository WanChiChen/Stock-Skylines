from django.shortcuts import render
from rest_framework import generics

from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

from .graph import find_max_city

@api_view(['POST'])
def stock_detail(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data = data)

        if serializer.is_valid():
            max_city = find_max_city(serializer.data['ticker'], serializer.data['period'], serializer.data['start'], serializer.data['end'], float(serializer.data['ratio']))
            res = {}
            res['similarity'] = max_city[0]
            print(max_city[1])
            res['data'] = max_city[1].to_json()
            return JsonResponse(res, status=status.HTTP_201_CREATED) 