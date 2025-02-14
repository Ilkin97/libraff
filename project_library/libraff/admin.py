from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.site_header = 'Libraff Admin'
admin.site.site_title = 'Libraff Admin Panel'
admin.site.index_title = 'Welcome to Libraff Admin Panel'

admin.site.register(Book)