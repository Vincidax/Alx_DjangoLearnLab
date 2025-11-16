from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filter sidebar for easy filtering
    list_filter = ('author', 'publication_year')

    # Enable search by title or author
    search_fields = ('title', 'author')

# Register your models here.
admin.site.register(Book, BookAdmin)