from django.urls import path
from .views import BookListView, BookDetailView, BookDetailSlugView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<slug:slug>/', BookDetailSlugView.as_view(), name='book-detail-slug'),
]