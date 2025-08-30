\# DELETE – Django Shell





\*\*Command run in Django shell:\*\*

```python

from bookshelf.models import Book

b = Book.objects.get(id=book.id)

b.delete()

Book.objects.all()

