from django.urls import path
from .api_views import BookListCreateView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]