from rest_framework import serializers
from datetime import date
from .models import Author, Book

# ----------------------------------------------
# BookSerializer
# Serializes all fields of the Book model.
# Custom validation ensures the publication year is not in the future.
# ----------------------------------------------
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validator for publication_year
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# ----------------------------------------------
# AuthorSerializer
# Serializes Author fields along with their related books.
# Uses a nested BookSerializer to include all books written by the author.
# The 'books' field uses the related_name from Book.author for reverse lookup.
# ----------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']
