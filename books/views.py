from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    # queryset = Book.objects.all()
    # serializer_class = BookSerializer
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()