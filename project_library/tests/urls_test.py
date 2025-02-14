from django.test import SimpleTestCase
from django.urls import reverse, resolve
from libraff.api.views import BookListView, BookDetailView, BookDetailSlugView

class URLTestCase(SimpleTestCase):

    def test_book_list_url(self):
        url = reverse('book-list')
        self.assertEqual(resolve(url).func.view_class, BookListView)

    def test_book_detail_url(self):
        url = reverse('book-detail', kwargs={'id': 1})
        self.assertEqual(resolve(url).func.view_class, BookDetailView)

    def test_book_detail_slug_url(self):
        url = reverse('book-detail-slug', kwargs={'slug': 'test-book'})
        self.assertEqual(resolve(url).func.view_class, BookDetailSlugView)