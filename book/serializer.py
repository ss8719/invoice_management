from rest_framework import serializers

from book.models import Author, AuthorProfile, Book, BookTopics


class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'author' in validated_data:
            raise serializers.ValidationError("Cannot update the 'author' field.")
        return super().update(instance, validated_data)


class BookTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTopics
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    topics = BookTopicsSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    userd = serializers.SerializerMethodField()
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['books', "userd"]

    def get_userd(self, obj):
        user = obj.user
        return {'username': user.username, 'email': user.email}
