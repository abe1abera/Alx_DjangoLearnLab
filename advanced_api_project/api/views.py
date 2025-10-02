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


    from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Book
from .serializers import BookSerializer

# Permission class used: authenticated users may create/update/delete,
# unauthenticated users may only read (list/retrieve).
SAFE_PERMISSION = permissions.IsAuthenticatedOrReadOnly


class BookListView(generics.ListAPIView):
    """
    GET /api/books/ -> list all books (readable by anyone)
    - supports search by title and ordering by publication_year
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [SAFE_PERMISSION]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']
    ordering = ['-publication_year']  # default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<pk>/ -> retrieve a single book by id (readable by anyone)
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [SAFE_PERMISSION]


class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/ -> create a new book (requires authentication)
    - Uses BookSerializer (which already validates publication_year).
    - We override perform_create to demonstrate custom hooks (logging, side-effects, etc.).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # only authenticated users can create

    def perform_create(self, serializer):
        # Example hook: could attach request.user to a "created_by" field if model had one.
        # For now, we simply save and return; this is where extra logic can go.
        book = serializer.save()
        # (Optional) Add side effects here (send signals, notifications, logging)
        return book


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<pk>/ -> update an existing book (requires authentication)
    - Only authenticated users can update.
    - Uses BookSerializer validation (including publication_year check).
    - We override perform_update to show where to add extra logic (audit logs, etc.).
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        book = serializer.save()
        # (Optional) add auditing or post-update behavior here
        return book


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<pk>/ -> delete a book (requires authentication)
    - Only authenticated users can delete.
    - You could refine this to IsAdminUser if deletion should be admin-only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # optional: custom deletion confirmation/soft-delete logic could go here
        return super().delete(request, *args, **kwargs)



# api/views.py
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

# Allow unauthenticated read, require auth for writes by default on read endpoints
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


# Required by the test: classes named CreateView, UpdateView, DeleteView
class CreateView(generics.CreateAPIView):
    """
    POST /api/books/create/ -> create a new Book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # hook for side effects (audit logs, signals, etc.)
        return serializer.save()


class UpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/<pk>/update/ -> update an existing Book (requires authentication)
    """
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # hook for post-update behavior
        return serializer.save()


class DeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<pk>/delete/ -> delete a Book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # place for custom deletion logic (soft-delete, audit, etc.)
        return super().delete(request, *args, **kwargs)
