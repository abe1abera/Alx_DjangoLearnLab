from django.contrib import admin
from .models import Author, Book

# Register models for admin UI so you can create Authors and Books via /admin/
admin.site.register(Author)
admin.site.register(Book)
