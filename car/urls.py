# urls.py
from django.urls import path

from car.views import create_showroom, get_all_showroom, create_car, get_all_cars, update_car_detail, get_car_detail, \
    add_show_room_details, get_all_users_show_room, get_all_showroom_which_have_car

urlpatterns = [
    path('create_showroom/', create_showroom, name='create_showroom'),
    path('get_all_showroom/', get_all_showroom, name='get_all_showroom'),
    path('create_car/', create_car, name='create_car'),
    path('get_all_cars/', get_all_cars, name='get_all_cars'),
    path('get_all_cars/', get_all_cars, name='get_all_cars'),
    path('get_car_detail/<int:car_id>/', get_car_detail, name='get_car_detail'),
    path('update_car_detail/<int:car_id>/', update_car_detail, name='update_car_detail'),
    path('add_show_room_details/', add_show_room_details, name='add_show_room_details'),
    path('get_all_users_show_room/', get_all_users_show_room, name='get_all_users_show_room'),
    path('get_all_showroom_which_have_car/', get_all_showroom_which_have_car, name='get_all_showroom_which_have_car'),
]
