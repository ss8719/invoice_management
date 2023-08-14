from django.urls import path

from book.views import create_author, get_authors, update_author, delete_author, create_author_profile, \
    get_author_profile, update_author_profile, create_book, get_books, test

urlpatterns = [
    path('create_author/', create_author, name='create_author'),
    path('get_authors/', get_authors, name='get_authors'),
    path('update_author/<int:author_id>/', update_author, name='update_author'),
    path('delete_author/<int:author_id>/', delete_author, name='delete_author'),
    path('create_author_profile/', create_author_profile, name='create_author_profile'),
    path('get_author_profile/', get_author_profile, name='get_author_profile'),
    path('update_author_profile/', update_author_profile, name='update_author_profile'),
    path('create_book/', create_book, name='create_book'),
    path('get_books/', get_books, name='get_books'),
    path('test/', test, name='test'),
]
