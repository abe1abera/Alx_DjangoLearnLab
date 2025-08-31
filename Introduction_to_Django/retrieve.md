# retrieve.md

```python
from bookshelf.models import Book
books = Book.objects.all()
list(books)
# Expected output:
# [<Book: 1984 by George Orwell (1949)>]

for book in Book.objects.all():
    print(book.title, book.author, book.publication_year)
# Expected output:
# 1984 George Orwell 1949