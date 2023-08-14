# serializers.py
from rest_framework import serializers

from a1.models import Review, Book, Author, Song


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text']


class BookSerializer(serializers.ModelSerializer):
    book_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'book_reviews']


class AuthorSerializer(serializers.ModelSerializer):
    author_books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'author_books']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
