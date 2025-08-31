from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=255, db_index=True)
    publication_year = models.PositiveIntegerField()

    class Meta:
        ordering = ["title"]  # default sort in admin and queries
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return f"{self.title} — {self.author} ({self.publication_year})"
