from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=200, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_as_author", )

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    email = models.EmailField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name="author_profile", )


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookTopics(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="topics", )
    topic = models.CharField(max_length=100)


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
