from django.shortcuts import render
from rest_framework import generics
from basic_api.models import DRFPost
from basic_api.serializers import DRFPostSerializer


class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
