# django-auto-model-loader

Django middleware that automatically resolves model instances from URL parameters like `user_pk`, `book_pk`, etc., and injects them into the `request` object.


---

## Usage

### Basic Example

For a URL like:

```
/api/books/<int:book_pk>/
```

The middleware will:

- Detect `book_pk` as a primary key
- Automatically search for the `Book` model across all installed Django apps
- Load `Book` model and inject it into `request.book`
- The model instance is loaded lazily — the database query runs only if `request.book` is used.

---

### Using Aliases

You can also register custom aliases for models if the default name doesn't match the actual class name.

```python
from django.db import models
from django_auto_model_loader import model_alias

@model_alias("example_book") 
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
```

This allows the middleware to resolve both of the following:

- `/api/books/<int:book_pk>/` → `request.book`
- `/api/books/<int:example_book_pk>/` → `request.book`
---

## ⚙️ Installation



## Setup
1. Install package
```bash
pip install django-auto-model-loader
```
2. Add middleware to your Django settings:
```python
INSTALLED_APPS = [
    ...,
    "django_auto_model_loader",
]

MIDDLEWARE = [
    ...,
    "django_auto_model_loader.middleware.AutoModelLoaderMiddleware",
]
```
---

## 📜 License
MIT © 2025 Dennis Tverdostup

