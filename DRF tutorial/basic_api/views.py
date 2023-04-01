from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def firstAPI(request):
    if request.method == 'GET':
        context = {
            'name': "Abu Bakkar Siddikk",
            'age': 25
        }
        return Response(context)

    elif request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        print("Hello Everyone")
        return Response({'name': name, 'age': age})
