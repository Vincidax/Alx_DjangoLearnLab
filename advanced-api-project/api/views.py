from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# ------------------------------------------------------------------
# BookListView
# ---------------------
# Generic ListAPIView:
# - Lists all Book instances in the database.
# - Anyone (authenticated or not) can access.
# - Read-only endpoint.
# ------------------------------------------------------------------
class BookListView(generics.ListAPIView):
    """
    BookListView:

    - Lists all Book instances with support for filtering, searching, and ordering.
    - Filtering:
        ?title=book_title
        ?author=author_id
        ?publication_year=year
    - Searching:
        ?search=keyword (searches in title and author's name)
    - Ordering:
        ?ordering=field_name
        ?ordering=-field_name (descending)
    - Permissions:
        IsAuthenticatedOrReadOnly (public can read, only authenticated users can write if extended)
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields (exact match)
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields (text search)
    search_fields = ['title', 'author__name']

    # Ordering fields (user can order by these)
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


# ------------------------------------------------------------------
# BookDetailView
# ---------------------
# Generic RetrieveAPIView:
# - Retrieves a single Book by primary key (id).
# - Anyone can access.
# - Read-only endpoint.
# ------------------------------------------------------------------
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ------------------------------------------------------------------
# BookCreateView
# ---------------------
# Generic CreateAPIView:
# - Allows authenticated users to create new Book instances.
# - Uses BookSerializer for validation and serialization.
# - Custom hook `perform_create` allows additional actions before saving.
# ------------------------------------------------------------------
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# ------------------------------------------------------------------
# BookUpdateView
# ---------------------
# Generic UpdateAPIView:
# - Allows authenticated users to update an existing Book by id.
# - Uses BookSerializer for validation and serialization.
# - Custom hook `perform_update` allows additional actions before saving.
# ------------------------------------------------------------------
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# ------------------------------------------------------------------
# BookDeleteView
# ---------------------
# Generic DestroyAPIView:
# - Allows authenticated users to delete a Book by id.
# - Ensures only authenticated users can perform deletion.
# ------------------------------------------------------------------
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
