from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Contact
from .serializers import ContactSerializer, ContactForm


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


@api_view(['GET', 'POST'])
def registrationAPI(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists', "username": username})
        else:
            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name, is_active=True)
                user.save()
                return Response({'message': 'User created successfully'})
            else:
                return Response({'message': 'Password does not match'})

    elif request.method == 'GET':
        users = User.objects.all()
        return Response({'message': 'This is get method', 'users': users})


# class ContactAPIView(APIView):
#     permission_classes = [AllowAny, ]
#
#     def post(self, request, format=None):
#         if request.method == 'POST':
#             name = request.data['name']
#             email = request.data['email']
#             subject = request.data['subject']
#             phone = request.data['phone']
#             details = request.data['details']
#             contact = Contact(name=name, email=email, phone=phone, subject=subject, details=details)
#             contact.save()
#             messages.success(request, 'Your message has been sent')
#             return Response({'message': 'Your message successfully saved', 'name': name, 'email': email})
#
#     def get(self, request, format=None):
#         if request.method == 'GET':
#             contacts = Contact.objects.all()
#             return Response({'message': 'This is get method', 'contacts': contacts})


class ContactAPIView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message': 'Invalid data'})

    def get(self):
        contacts = Contact.objects.all()
        return Response({'message': 'This is get method', 'contacts': contacts})
