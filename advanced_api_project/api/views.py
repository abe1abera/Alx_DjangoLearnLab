# api/views.py
from rest_framework import viewsets, generics, permissions, filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Keep your ViewSets (optional) — tests may ignore them but it's fine to keep.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer


# Generic views required by checks: exact class names below
SAFE_PERMISSION = permissions.IsAuthenticatedOrReadOnly

class ListView(generics.ListAPIView):
    """
    Read-only list of books (anyone can read).
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [SAFE_PERMISSION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']
    ordering = ['-publication_year']


class DetailView(generics.RetrieveAPIView):
    """
    Read-only detail of a book (anyone can read).
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [SAFE_PERMISSION]


class CreateView(generics.CreateAPIView):
    """
    Create a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()


class UpdateView(generics.UpdateAPIView):
    """
    Update a book (authenticated users only).
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        return serializer.save()


class DeleteView(generics.DestroyAPIView):
    """
    Delete a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
