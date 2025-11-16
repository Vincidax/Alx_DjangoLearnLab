# relationship_app/urls.py

from django.urls import path
from .views import list_books
from .views import user_login, user_logout, register, LibraryDetailView

urlpatterns = [
    # Authentication URLs
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

    # Function-Based View (FBV)
    path('books/', list_books, name='list_books'),

    # Class-Based View (CBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
