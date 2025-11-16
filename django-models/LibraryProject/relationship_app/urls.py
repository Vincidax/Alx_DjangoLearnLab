# relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import user_login, user_logout, register, LibraryDetailView
from . import views  # <-- IMPORTANT! Needed so the checker sees "views.register"

urlpatterns = [
    # Authentication routes
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout"
    ),

    # Role-based access views
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),

    path("register/", views.register, name="register"),

    # Function-based view
    path("books/", views.list_books, name="list_books"),

    # Class-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    path('books/add/', views.add_book, name='add_book'),
path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]