from django.urls import path
from .views import ProductDetailsAPIView, ProductRetrieveUpdateDestroyAPIViewDetails, search

urlpatterns = [
    path('', ProductRetrieveUpdateDestroyAPIViewDetails.as_view()),
    path('<int:pk>', ProductDetailsAPIView.as_view()),
    path('search/', search, name='search'),
]
