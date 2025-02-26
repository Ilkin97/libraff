# Library Management System

A modern and efficient Library Management System built with Django and Django REST Framework, designed to streamline book inventory management and provide RESTful API endpoints for integration.

---

## Key Features

- REST API endpoints for book management
- Django Admin interface integration
- Slug-based URL routing
- Custom management command for data ingestion
- Comprehensive test coverage
- Pipenv-based dependency management

---

## Installation

### Prerequisites
- Python 3.9+
- Pipenv
- PostgreSQL (recommended)

### Setup Instructions

1. **Clone Repository**
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. **Install Dependencies**
   ```bash
   pipenv install
   ```

3. **Configure Database**
   - Update database settings in `project_library/settings.py`.
   - Create a PostgreSQL database (if using).

4. **Run Migrations**
   ```bash
   pipenv run python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   pipenv run python manage.py createsuperuser
   ```

6. **Load Sample Data (Optional)**
   ```bash
   pipenv run python manage.py load_books books_data.json
   ```

7. **Start Development Server**
   ```bash
   pipenv run python manage.py runserver
   ```

---

## API Documentation

### Base URL: `http://localhost:8000/api/`

| Endpoint              | Method | Description            |
|-----------------------|--------|------------------------|
| `/books/`             | GET    | List all books         |
| `/books/`             | POST   | Create a new book      |
| `/books/<int:id>/`    | GET    | Retrieve book by ID    |
| `/books/<int:id>/`    | PUT    | Update book by ID      |
| `/books/<int:id>/`    | DELETE | Delete book by ID      |
| `/books/<slug:slug>/` | GET    | Retrieve book by slug  |

**Example Request:**
```bash
curl -X GET http://localhost:8000/api/books/1/
```

---

## Admin Interface

Access the Django Admin panel at `http://localhost:8000/admin/` using your superuser credentials to:
- Manage book records
- View user activity
- Modify system configurations

---

## Testing

Run the test suite with:
```bash
pipenv run python manage.py test
```

Test coverage includes:
- Model validation
- API endpoints
- Serializers
- URL routing
- View permissions

---

## Project Structure

```plaintext
Library/
├── project_library/
│   ├── libraff/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   ├── management/
│   │   │   ├── commands/
│   │   │   │   ├── load_books.py
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_api.py
│   │   │   ├── test_models.py
│   │   │   ├── test_serializers.py
│   │   │   ├── test_urls.py
│   │   │   ├── test_views.py
│   ├── project_library/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
├── requirements.txt
```

---

## Dependencies

- Django 4.2+
- Django REST Framework 3.14+
- Python Slugify 8.0+
- Psycopg2 (PostgreSQL adapter)

Install requirements:
```bash
pip install -r requirements.txt
```

---

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE). Make sure to include the appropriate license file.

---

"""