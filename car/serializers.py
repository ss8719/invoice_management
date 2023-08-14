from rest_framework import serializers

from car.models import Showroom, Car, ShowroomDetails
from users_api.serializers import UserSerializer


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = '__all__'

    def to_internal_value(self, data):
        data = super(ShowroomSerializer, self).to_internal_value(data)
        return data


class CarSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'

    def to_representation(self, instance):
        data = super(CarSerializer, self).to_representation(instance)
        # data['nothing'] = UserSerializer(instance.created_by).data
        return data


class ShowroomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomDetails
        fields = '__all__'
