# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer