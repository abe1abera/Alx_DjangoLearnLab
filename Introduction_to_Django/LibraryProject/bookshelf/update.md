# update.md

```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk)
# Expected output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>