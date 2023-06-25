from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .seriallizers import ProductSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView


class ProductDetailsAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
