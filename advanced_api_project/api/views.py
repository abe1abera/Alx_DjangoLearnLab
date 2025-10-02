# api/views.py
from rest_framework import viewsets, generics, permissions, filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# -------------------------
# ViewSets (keep if you use routers elsewhere)
# -------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for authors: list, create, retrieve, update, destroy.
    """
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for books: list, create, retrieve, update, destroy.
    (Optional — you can remove this if you prefer the generic views only.)
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer


# -------------------------
# Generic views (module-level: tests expect the names below)
# -------------------------
SAFE_PERMISSION = permissions.IsAuthenticatedOrReadOnly

class ListView(generics.ListAPIView):
    """
    GET /api/books/ -> list all books (readable by anyone)
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
    GET /api/books/<pk>/ -> retrieve a single book by id (readable by anyone)
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [SAFE_PERMISSION]


class CreateView(generics.CreateAPIView):
    """
    POST /api/books/create/ -> create a new Book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()


class UpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<pk>/update/ -> update an existing Book (requires authentication)
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        return serializer.save()


class DeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<pk>/delete/ -> delete a Book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return
