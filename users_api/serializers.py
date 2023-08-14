import uuid

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email address already exists.")
        return value

    def create(self, validated_data):
        # Generate a unique username using UUID4
        username = uuid.uuid4().hex[:30]
        validated_data['username'] = username

        # Call the superclass's create method to create the user instance
        user = super().create(validated_data)

        # Set the user's password using set_password to hash it
        user.set_password(validated_data['password'])

        # Save the user instance to the database
        user.save()
        return user

    def login(self, email, password):
        user = authenticate(request=self.context.get('request'), username=email, password=password)
        if user is not None:
            return user
        raise serializers.ValidationError("Invalid email or password.")
