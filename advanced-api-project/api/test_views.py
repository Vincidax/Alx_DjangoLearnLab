from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # --------------------------
        # Create test user and token
        # --------------------------
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token, _ = Token.objects.get_or_create(user=self.user)

        # --------------------------
        # Login using Django test client
        # --------------------------
        self.client.login(username='testuser', password='testpass')

        # --------------------------
        # Create authors
        # --------------------------
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George Orwell')

        # --------------------------
        # Create books
        # --------------------------
        self.book1 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author2
        )

        # --------------------------
        # API URLs
        # --------------------------
        self.list_url = reverse('books-list')
        self.create_url = reverse('books-create')
        self.detail_url = lambda pk: reverse('books-detail', kwargs={'pk': pk})
        self.update_url = lambda pk: reverse('books-update', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse('books-delete', kwargs={'pk': pk})

    # --------------------------
    # Helper: authenticate client with token
    # --------------------------
    def authenticate_with_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # --------------------------
    # Test: List all books
    # --------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # --------------------------
    # Test: Retrieve single book
    # --------------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # --------------------------
    # Test: Create book (authenticated)
    # --------------------------
    def test_create_book_authenticated(self):
        self.authenticate_with_token()
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'New Book')

    # --------------------------
    # Test: Create book (unauthenticated)
    # --------------------------
    def test_create_book_unauthenticated(self):
        self.client.logout()  # remove session login
        self.client.credentials()  # remove token
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])
        self.assertEqual(Book.objects.count(), 2)

    # --------------------------
    # Test: Update book (authenticated)
    # --------------------------
    def test_update_book_authenticated(self):
        self.authenticate_with_token()
        data = {
            'title': 'Updated Title',
            'publication_year': 1997,
            'author': self.author1.id
        }
        response = self.client.put(self.update_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    # --------------------------
    # Test: Delete book (authenticated)
    # --------------------------
    def test_delete_book_authenticated(self):
        self.authenticate_with_token()
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --------------------------
    # Test: Filtering by title
    # --------------------------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': "1984"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    # --------------------------
    # Test: Searching by author
    # --------------------------
    def test_search_books_by_author(self):
        response = self.client.get(self.list_url, {'search': 'Rowling'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    # --------------------------
    # Test: Ordering by publication_year
    # --------------------------
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)
