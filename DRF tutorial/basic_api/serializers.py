from django import forms
from rest_framework import serializers
from .models import Contact, BlogPost


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'email', 'phone', 'subject', 'details']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = ['title', 'details']
