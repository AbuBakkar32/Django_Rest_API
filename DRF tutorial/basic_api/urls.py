from django.urls import path
from .views import *

urlpatterns = [
    path('firstapi/', firstAPI),
    path('registration/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
    path('post/', PostCreatedAPIView.as_view()),
]
