# relationship_app/query_samples.py

import os
import sys
import django

# Ensure Python can find the inner LibraryProject package
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Import models
from relationship_app.models import Author, Book, Library, Librarian

# ---------------------------
# Query all books by a specific author
# ---------------------------
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Use objects.filter instead of related_name
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author_name}:")
        if books.exists():
            for book in books:
                print(f"- {book.title}")
        else:
            print("No books found for this author.")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'")

# ---------------------------
# List all books in a library
# ---------------------------
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")

# ---------------------------
# Retrieve the librarian for a library
# ---------------------------
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Use objects.get instead of reverse OneToOne
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'")

# ---------------------------
# Example usage
# ---------------------------
if __name__ == "__main__":
    books_by_author("George Orwell")
    books_in_library("Central Library")
    librarian_for_library("Central Library")
