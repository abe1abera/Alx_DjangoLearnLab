\# UPDATE – Django Shell





\*\*Command run in Django shell:\*\*

```python

from bookshelf.models import Book

b = Book.objects.get(id=book.id)

b.title = "Nineteen Eighty-Four"

b.save()

print(b.id, b.title, b.author, b.publication\_year)

