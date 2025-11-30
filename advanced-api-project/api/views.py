from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
        """
        Override perform_create to customize behavior on book creation.
        Currently, it simply saves the validated book instance.
        Additional hooks (logging, setting extra fields) can be added here.
        """
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
        """
        Override perform_update to customize behavior on book update.
        Currently, it simply saves the validated book instance.
        """
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
