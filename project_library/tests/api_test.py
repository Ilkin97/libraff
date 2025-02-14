from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from libraff.models import Book
from libraff.api.serializers import BookSerializer

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description",
            published_date="2025-02-14",
            slug="test-book"
        )
        self.book_data = {
            "title": "New Book",
            "author": "New Author",
            "description": "New Description",
            "published_date": "2025-02-14",
            "slug": "new-book"
        }

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        url = reverse('book-list')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, self.book_data['title'])

    def test_get_book_detail(self):
        url = reverse('book-detail', kwargs={'id': self.book.id})
        response = self.client.get(url)
        book = Book.objects.get(id=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'id': self.book.id})
        updated_data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "description": "Updated Description",
            "published_date": "2025-02-14",
            "slug": "updated-book"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_data['title'])

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'id': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_get_book_detail_by_slug(self):
        url = reverse('book-detail-slug', kwargs={'slug': self.book.slug})
        response = self.client.get(url)
        book = Book.objects.get(slug=self.book.slug)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)