import json
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.seriallizers import ProductSerializer


# Create your views here.
@api_view(["GET"])
def api_view(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if request.method == "POST":
        if serializer.is_valid:
            instance = serializer.save()
            print(serializer.data)
            data = serializer.data
            return Response(data)
    if request.method == "GET":
        data = Product.objects.all().order_by("id")
        print(data)
        return JsonResponse(data)
    # return Response({"Invalid": "Not Get Data"}, status=400)

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
