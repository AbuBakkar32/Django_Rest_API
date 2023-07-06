from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .seriallizers import ProductSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter


# API views for product details and product list
class ProductDetailsAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


# Product Retrieve Update Destroy API Generic View
class ProductRetrieveUpdateDestroyAPIViewDetails(RetrieveUpdateDestroyAPIView):
    """
    Api view queryset and serializer_class used to get the data
    and serializer_class call will help to convert the object
    data into the json format
    """
    print("Hello Django Rest API")
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Search view for search form
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})
