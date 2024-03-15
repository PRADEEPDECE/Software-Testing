# crud_app/urls.py
from django.urls import path
from .views import ItemListCreateAPIView, ItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('items/', ItemListCreateAPIView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail'),
]
