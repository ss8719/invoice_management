from django.urls import path

from a1.views import book_list, add_song

urlpatterns = [
    path('', book_list, name='books'),
    path('add_song/', add_song, name='add_song'),

]
