import json
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.seriallizers import ProductSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView


def api_view(request, *args, **kwargs):
    if request.method == 'GET':
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# def api_view(request, *args, **kwargs):
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     print(data)
#     return JsonResponse(data)
