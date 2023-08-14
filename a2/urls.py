from django.urls import path

from a2.views import post_user, posts, assign_task, unassign_task

urlpatterns = [
    path('', post_user, name='post_user'),
    path('posts/', posts, name='posts'),
    path('assign_task/<int:task_id>/<int:user_id>/', assign_task, name='assign_task'),
    path('unassign_task/<int:task_id>/<int:user_id>/', unassign_task, name='unassign_task'),
    # path('add_song/', add_song, name='add_song'),

]
