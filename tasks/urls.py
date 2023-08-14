# urls.py
from django.urls import path

from .views import task_list_create_view, task_retrieve_update_delete_view, create_task_assignment, delete_task, \
    get_all_task, get_all_task_assigned_to_me

urlpatterns = [
    path('', task_list_create_view, name='task-list-create'),
    path('<int:pk>/', task_retrieve_update_delete_view, name='task-retrieve-update-delete'),
    path('assign_task/', create_task_assignment, name='create_task_assignment'),
    path('delete_task/', delete_task, name='delete_task'),
    path('get_all_task/', get_all_task, name='get_all_task'),
    path('get_all_task_assigned_to_me/', get_all_task_assigned_to_me, name='get_all_task_assigned_to_me'),
]
