## Create
```python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b
# <Book: 1984 by George Orwell (1949)>
```

## Retrieve
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)
```

## Update
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(pk=book.pk)
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
```

## Delete
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# (1, {'bookshelf.Book': 1})
list(Book.objects.all())
# []
```
