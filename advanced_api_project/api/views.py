from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for authors: list, create, retrieve, update, destroy.
    AuthorSerializer returns nested books for each author.
    """
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for books: list, create, retrieve, update, destroy.
    BookSerializer validates publication_year.
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
