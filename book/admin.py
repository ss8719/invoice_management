# Register your models here.
from django.contrib import admin

from book.models import Author, Book, BookTopics

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookTopics)
