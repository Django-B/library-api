from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
	'''
	Класс, который обрабатывает: 
	GET запрос для получения списка объектов книг,
	POST запрос для создания нового объекта книги
	'''
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	'''
	Класс, который обрабатывает запросы:
	GET для получения одного объекта книги,
	PUT для обновления объекта книги,
	DELETE для удаления объекта книги.
	'''
	queryset = Book.objects.all()
	serializer_class = BookSerializer