from django.db import models

# ----------------------------------------------
# Author model
# Represents a book author.
# Fields:
#   - name: stores the author's full name.
# Relationships:
#   - One author can have many books (one-to-many)
# ----------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=255)  # CharField requires max_length

    def __str__(self):
        # Makes Author objects readable in admin and shell
        return self.name


# ----------------------------------------------
# Book model
# Represents a book in the database.
# Fields:
#   - title: the book's title
#   - publication_year: year the book was published
#   - author: foreign key linking to Author (one-to-many relationship)
# Relationships:
#   - Each book belongs to one author
#   - If an author is deleted, all their books are deleted (CASCADE)
# ----------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,      # Delete books if the author is deleted
        related_name='books'           # Allows reverse lookup: author.books.all()
    )

    def __str__(self):
        # Makes Book objects readable in admin and shell
        return f"{self.title} ({self.publication_year})"
