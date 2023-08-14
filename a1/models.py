from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author_books", editable=False)


class Review(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_reviews", editable=False)


class Song(models.Model):
    author = models.ManyToManyField(Author, related_name="author_all_songs")
    song_name = models.CharField(max_length=100)
