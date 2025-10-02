from django.db import models

class Author(models.Model):
    """
    Author model:
    - Represents an author who may have many books (one-to-many relation).
    - Fields:
      - name: the full name of the author (string).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - Stores information about a book and references its Author.
    - Fields:
      - title: book title (string).
      - publication_year: integer year the book was published.
      - author: ForeignKey to Author, creating Author -> Books (one-to-many).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # allows accessing author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
