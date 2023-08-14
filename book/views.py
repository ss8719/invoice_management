from django.contrib.auth.models import User
from django.db.models import Prefetch, Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from book.models import Author, Book
from book.serializer import AuthorSerializer, AuthorProfileSerializer, BookSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_author(request):
    request.data["user"] = request.user.id
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_authors(request):
    authors_with_books_and_topics = Author.objects.prefetch_related(
        Prefetch('books',
                 queryset=Book.objects.filter(Q(author_id=13)).prefetch_related(
                     'topics'))
    )
    serializer = AuthorSerializer(authors_with_books_and_topics)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_author(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        return Response({"detail": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AuthorSerializer(author, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_author_profile(request):
    author: Author = request.user.user_as_author
    request.data["author"] = author.id
    serializer = AuthorProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_author_profile(request):
    author = request.user.user_as_author
    serializer = AuthorProfileSerializer(author.author_profile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_author_profile(request):
    author = request.user.user_as_author
    serializer = AuthorProfileSerializer(author.author_profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user.user_as_author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def get_books(request):
    authors = Author.objects.prefetch_related('books')

    author_data = []
    for author in authors:
        books = [{'title': book.title} for book in author.books.all()]
        author_data.append({
            'id': author.id,
            'name': author.name,
            'profile_url': author.profile_url,
            'books': books
        })
    return Response(author_data)


@api_view(["GET", "POST"])
def test(request):
    if request.method == "POST":

        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=User.objects.get(id=6))
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if request.method == "GET":
        return Response("serializer.data")
