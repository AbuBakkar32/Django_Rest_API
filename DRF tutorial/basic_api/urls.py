from django.urls import path
from .views import *

urlpatterns = [
    path('firstapi/', firstAPI),
    path('registration/', registrationAPI),
]
