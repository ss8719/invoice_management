# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from a1.models import Author
from a1.serializers import BookSerializer, AuthorSerializer, ReviewSerializer, SongSerializer


@api_view(["GET", 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Author.objects.prefetch_related("author_books__book_reviews").all()
        serializer = AuthorSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        author_serializer = AuthorSerializer(data=request.data)
        if author_serializer.is_valid():
            book_serializer = BookSerializer(data=request.data)
            if book_serializer.is_valid():
                review_serializer = ReviewSerializer(data=request.data)
                if review_serializer.is_valid():
                    author = author_serializer.save()
                    book = book_serializer.save(author=author)
                    review_serializer.save(book=book)
                    return Response(author_serializer.data, status=status.HTTP_201_CREATED)
                return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def add_song(request):
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
