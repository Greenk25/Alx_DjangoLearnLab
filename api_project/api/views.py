from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer to serialize data
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  # Fetch all Book objects from the database
    serializer_class = BookSerializerI
