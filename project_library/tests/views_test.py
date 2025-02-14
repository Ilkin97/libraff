from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from libraff.models import Book

class BookViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        url = reverse('book-list')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book_detail(self):
        url = reverse('book-detail', kwargs={'id': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'id': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)