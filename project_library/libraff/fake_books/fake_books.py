import json
from faker import Faker
import random


fake = Faker()


books = []


for _ in range(100):
    book = {
        "title": fake.sentence(nb_words=random.randint(2, 5)).rstrip('.'),
        "author": fake.name(),
        "description": fake.paragraph(nb_sentences=random.randint(3, 6)),
        "published_date": fake.date_between(start_date='-30y', end_date='today').isoformat(),
        "slug": fake.slug()
    }
    books.append(book)


with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

print("Successfully created 100 fake books")
