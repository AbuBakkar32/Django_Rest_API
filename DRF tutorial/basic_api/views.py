from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .models import Contact, BlogPost
from .serializers import ContactSerializer, ContactForm, PostSerializer
# Token - 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

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


# Class based API View
class ContactAPIView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message': 'Invalid data'})

    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


# Generic API View
class PostCreatedAPIView(ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return BlogPost.objects.filter(is_active=True)


class PostRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny, ]
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
