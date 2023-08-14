# urls.py
from django.urls import path

from todos.views import create_todo, get_all_todo, get_all_todo_created_by_user, assign_todo, \
    get_all_assigned_todo_to_user

urlpatterns = [
    path('create_todo/', create_todo, name='create_todo'),
    path('get_all_todo/', get_all_todo, name='get_all_todo'),
    path('get_all_todo_created_by_user/', get_all_todo_created_by_user, name='get_all_todo_created_by_user'),
    path('assign_todo/', assign_todo, name='assign_todo'),
    path('get_all_assigned_todo_to_user/', get_all_assigned_todo_to_user, name='get_all_assigned_todo_to_user'),

    # path('get_all_assigned_todo/', get_all_assigned_todo, name='get_all_assigned_todo'),
    # path('get_all_assigned_todo_user/', get_all_assigned_todo_user, name='get_all_assigned_todo_user'),

]
