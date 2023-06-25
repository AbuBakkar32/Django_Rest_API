from django.urls import path
from .views import ProductDetailsAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:pk>', ProductDetailsAPIView.as_view()),
]
