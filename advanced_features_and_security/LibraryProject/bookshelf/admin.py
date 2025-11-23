from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

# ----------------------------
# CustomUser admin
# ----------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

# Register CustomUser with admin
admin.site.register(CustomUser, CustomUserAdmin)

# ----------------------------
# Book admin
# ----------------------------
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register Book model
admin.site.register(Book, BookAdmin)

# ----------------------------
# Optional: register other models
# ----------------------------
# admin.site.register(Author)
# admin.site.register(Library)
# admin.site.register(Librarian)
