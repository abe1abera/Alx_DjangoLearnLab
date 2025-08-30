\### 6.5 `CRUD\_operations.md` (combined)

Create `Introduction\_to\_Django/CRUD\_operations.md` with:

```md

\# CRUD Operations – Django Shell (bookshelf.Book)





\## CREATE

```python

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book

