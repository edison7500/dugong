from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model       = Book
        fields      = ('title', 'desc', 'price', 'asin',
                        'origin_link', 'create_datetime', 'images')
        extra_kwargs = {'asin': {'write_only': True}}

    #
    # def create(self, validated_data):
    #     obj     = super(BookSerializer, self).create(validated_data)
    #
    #     return obj

