from rest_framework import serializers
from datetime import date
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model.
    - All model fields are included.
    - Custom validation ensures publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['id']

    def validate_publication_year(self, value):
        """
        Ensure the publication_year is not in the future.
        Raises a ValidationError if the year > current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication_year ({value}) cannot be in the future (current year: {current_year})."
            )
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """
    Internal nested serializer for presenting book data inside the AuthorSerializer.
    This serializer is read-only in the nested context.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model.
    - Includes 'name' and a nested list of books (using NestedBookSerializer).
    - The 'books' field is populated via the Author.books related_name.
    - By default the nested books are read-only; author creation/updates expect
      books to be created/updated via the Book endpoints (or you can extend this
      serializer to support writable nested create/update).
    """
    books = NestedBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        read_only_fields = ['id']
