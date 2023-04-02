from django.urls import path
from .views import *

urlpatterns = [
    path('firstapi/', firstAPI),
    path('registration/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
    path('post/', PostCreatedAPIView.as_view()),
    path('post/<int:id>/', PostRetrieveAPIView.as_view()),
    path('post/update/<int:id>/', PostRetrieveUpdateAPIView.as_view()),
]
