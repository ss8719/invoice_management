# Create your views here.
# user_api/views.py

from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .backends import User
from .serializers import UserSerializer


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    serializer = UserSerializer()
    try:
        # Check if the user with the provided email exists
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email does not exist.")

        user = serializer.login(email=email, password=password)

        # Generate tokens using djangorestframework-simplejwt
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    except serializers.ValidationError as e:
        return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
