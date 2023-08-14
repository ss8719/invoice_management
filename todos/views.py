from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todos.models.todo_assign_model import TodoAssignSerializer
from todos.models.todo_model import TodoSerializer, Todo


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by_user_id=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_todo(request):
    todos = Todo.objects.all().order_by('-created_at')
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_todo_created_by_user(request):
    user: User = request.user
    todos = user.users_created_todos.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_todo(request):
    serializer = TodoAssignSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(assigned_by_user_id=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_assigned_todo_to_user(request):
    user: User = request.user
    data = user.assigned_to_user.all()
    serializer = TodoAssignSerializer(data, many=True)
    return Response(serializer.data, status=201)
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_todo(request):
#     serializer = TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(created_by_user_id=request.user)
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_all_todo(request):
#     todo = Todo.objects.all()
#     serializer = TodoSerializer(todo, many=True)
#
#     return Response(serializer.data, status=201)
#
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def assign_todo(request):
#     serializer = TodoAssignSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(assigned_by_user_id=request.user)
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
#
#
# # Create your views here.
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_all_assigned_todo(request):
#     todo = TodoAssign.objects.all()
#     serializer = TodoAssignSerializer(todo, many=True)
#
#     return Response(serializer.data, status=201)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_all_assigned_todo_user(request):
#     user: User = request.user  # The authenticated user making the request
#     user_serializer = UserSerializer(user)
#     assigned_todos = user.created_by_user_id.all()
#     todo_serializer: TodoSerializer = TodoSerializer(assigned_todos, many=True)
#
#     response_data = {
#         # 'user': user_serializer.data,
#         'assigned_todos': todo_serializer.data,
#     }
#
#     return Response(response_data, status=200)
