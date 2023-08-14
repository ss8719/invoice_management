from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from a2.models import User, Task
from a2.serializers import UserSerializer, TaskSerializer


# Create your views here.
@api_view(["GET", "POST"])
def post_user(request):
    if request.method == "GET":
        post_users = User.objects.all()
        serializer = UserSerializer(post_users, many=True)
        return Response(serializer.data)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(["GET", "POST"])
def posts(request):
    if request.method == "GET":
        posts = Task.objects.all()
        serializer = TaskSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(['POST'])
def assign_task(request, task_id, user_id):
    try:
        task = Task.objects.get(pk=task_id)
        user = User.objects.get(pk=user_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    task.assigned_to.add(user)
    task.save()

    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def unassign_task(request, task_id, user_id):
    try:
        task = Task.objects.get(pk=task_id)
        user = User.objects.get(pk=user_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    task.assigned_to.remove(user)
    task.save()

    serializer = TaskSerializer(task)
    return Response(serializer.data)
