from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from car.models import Showroom, Car
from car.serializers import ShowroomSerializer, CarSerializer, ShowroomDetailsSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_showroom_which_have_car(request):
    books_with_authors = Car.objects.select_related('created_by').all()
    for b in books_with_authors:
        print(b)
    # queryset = Showroom.objects.filter(book__isnull=False).distinct()
    serializer = CarSerializer(books_with_authors, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_users_show_room(request):
    # user = request.user
    # user.show_room_created_by_user.all()
    books_with_authors = Showroom.objects.select_related("created_by").all()
    serializer = ShowroomSerializer(books_with_authors, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_show_room_details(request):
    serializer = ShowroomDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_car_detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)  # Retrieve the car by its primary key
    except Car.DoesNotExist:
        raise NotFound("Car not found")

    serializer = CarSerializer(car)  # Serialize the single car instance
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_car_detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)  # Retrieve the car by its primary key
    except Car.DoesNotExist:
        raise NotFound("Car not found")

    serializer = CarSerializer(car, data=request.data)  # Serialize the single car instance
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_cars(request):
    query = Car.objects.all()
    serializer = CarSerializer(query, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_showroom(request):
    request.data['created_by'] = request.user.id
    serializer = ShowroomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_showroom(request):
    query = Showroom.objects.all()
    serializer = ShowroomSerializer(query, many=True)
    return Response(serializer.data)
