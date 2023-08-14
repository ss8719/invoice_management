# Create your views here.
# views.py

from rest_framework import status
# tasks/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task, TaskAssignment
from .serializers import TaskAssignmentSerializer
from .serializers import TaskSerializer


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_task_assigned_to_me(request):
    tasks = TaskAssignment.objects.all()
    serializer = TaskAssignmentSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_task(request):
    tasks = Task.objects.filter(task_assignments__isnull=False).order_by('id').distinct()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, ):
    try:
        task = Task.objects.get(id=request.data["task_id"])
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task_assignment(request):
    serializer = TaskAssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(assigned_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list_create_view(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associate the task with the current authenticated user
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_retrieve_update_delete_view(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found.'}, status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)
