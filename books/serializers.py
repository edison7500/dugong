from rest_framework import serializers
from books.models import Book, Image


class BookSerializer(serializers.HyperlinkedModelSerializer):
    image_urls      = serializers.ListField(required=False)

    class Meta:
        model       = Book
        fields      = ('url','title', 'desc', 'price', 'asin',
                        'origin_link', 'create_datetime', 'image_urls')
        extra_kwargs = {
            'asin': {'write_only': True},
            'url': {'lookup_field':'asin'},
        }

    def create(self, validated_data):
        # print validated_data['image_urls']
        obj         = super(BookSerializer, self).create(validated_data)
        image_urls  = validated_data.get('image_urls')
        if image_urls:
            data    = list()
            for path in image_urls:
                data.append(
                    Image(book=obj, image=path)
                )
            Image.objects.bulk_create(
                data
            )
        return obj

