import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from libraff.models import Book

class Command(BaseCommand):
    help = 'Load books from a JSON file into the database'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'libraff', 'json', 'books.json')
        try:
            with open(file_path, 'r') as file:
                books_data = json.load(file)
                for book_data in books_data:
                    book, created = Book.objects.get_or_create(
                        title=book_data['title'],
                        author=book_data['author'],
                        description=book_data['description'],
                        published_date=book_data['published_date'],
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Book '{book.title}' added successfully"))
                    else:
                        self.stdout.write(self.style.SUCCESS(f"Book '{book.title}' already exists"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File '{file_path}' not found"))