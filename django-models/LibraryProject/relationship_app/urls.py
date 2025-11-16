from django.urls import path
from .views import user_login, user_logout, register, list_books, LibraryDetailView

urlpatterns = [
    # Authentication URLs
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

    # Book and Library Views
    path('books/', list_books, name='list_books'),  # ✅ Explicit import for FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
