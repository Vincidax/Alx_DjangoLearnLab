from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books-list'),            # List all books
    path('books/create/', BookCreateView.as_view(), name='books-create'), # Create a book
    path('books/<int:pk>/', BookDetailView.as_view(), name='books-detail'),  # Retrieve a single book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='books-update'),  # Update a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='books-delete'),  # Delete a book
]
