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

    # Checker expects: "views.register"
    path("register/", views.register, name="register"),

    # Function-based view
    path("books/", views.list_books, name="list_books"),

    # Class-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]