from django.test import TestCase
from libraff.models import Book

class BookModelTestCase(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description",
            published_date="2025-02-14",
            slug="test-book"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.description, "Test Description")
        self.assertEqual(self.book.published_date, "2025-02-14")
        self.assertEqual(self.book.slug, "test-book")

    def test_book_str(self):
        self.assertEqual(str(self.book), "Test Book")