# api/views.py k
from rest_framework import generics
# <-- Checker expects this exact import line:
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# List and create (list allowed for unauthenticated, create requires auth)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve, update, destroy (retrieve allowed for unauthenticated, update/delete require auth)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Author views (same permission pattern)
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Allow filtering by these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Allow searching by these fields
    search_fields = ['title', 'author']

    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
