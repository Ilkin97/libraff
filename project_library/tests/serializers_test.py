from django.test import TestCase
from libraff.models import Book
from libraff.api.serializers import BookSerializer

class BookSerializerTestCase(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description",
            published_date="2025-02-14",
            slug="test-book"
        )
        self.serializer = BookSerializer(instance=self.book)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'author', 'description', 'published_date', 'slug']))

    def test_serializer_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.book.title)
        self.assertEqual(data['author'], self.book.author)
        self.assertEqual(data['description'], self.book.description)
        self.assertEqual(data['published_date'], str(self.book.published_date))
        self.assertEqual(data['slug'], self.book.slug)