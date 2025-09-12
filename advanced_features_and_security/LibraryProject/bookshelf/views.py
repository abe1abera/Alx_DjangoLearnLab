# views.py (inside bookshelf app)

from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    output = ", ".join([f"{book.title} by {book.author}" for book in books])
    return HttpResponse(f"Books: {output}")


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # For simplicity, just create a dummy book entry
    Book.objects.create(title="New Book", author="Unknown Author")
    return HttpResponse("Book created successfully!")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.title = "Edited Title"
        book.save()
        return HttpResponse("Book edited successfully!")
    except Book.DoesNotExist:
        return HttpResponse("Book not found.")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return HttpResponse("Book deleted successfully!")
    except Book.DoesNotExist:
        return HttpResponse("Book not found.")
