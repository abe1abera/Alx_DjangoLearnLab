# CRUD_operations.md

from bookshelf.models import Book

# --- CREATE ---
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b
# Expected output:
# <Book: 1984 by George Orwell (1949)>

# --- RETRIEVE ---
books = Book.objects.all()
list(books)
# Expected output:
# [<Book: 1984 by George Orwell (1949)>]

for book in Book.objects.all():
    print(book.title, book.author, book.publication_year)
# Expected output:
# 1984 George Orwell 1949

# --- UPDATE ---
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk)
# Expected output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

# --- DELETE ---
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
list(Book.objects.all())
# Expected output:
# []
