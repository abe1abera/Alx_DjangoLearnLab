\# RETRIEVE – Django Shell





\*\*Command run in Django shell:\*\*

```python

from bookshelf.models import Book

b = Book.objects.get(id=book.id) # alternative: Book.objects.get(title="1984")

print(b.id, b.title, b.author, b.publication\_year)

