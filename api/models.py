from django.db import models

class Author(models.Model):
    """
    Author model:
    - name: stores the author's name.
    This model is the "one" side of a one-to-many relationship (Author -> Book).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - title: title of the book
    - publication_year: integer year when the book was published
    - author: ForeignKey to Author. related_name='books' lets us access an author's books
      with `author.books.all()`. on_delete=models.CASCADE removes books if the author
      is deleted (logical for this sample app).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
