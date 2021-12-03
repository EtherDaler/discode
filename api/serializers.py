from rest_framework import serializers
from mainApp.models import *
import datetime

def default_datetime():
    return datetime.datetime.now()


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('__all__')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("__all__")

class DiscountsSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Discounts
        fields = (
            'id',
            'partner',
            'name',
            'body',
            'discount',
            'slug',
            'category',
            'date_of_create',
            'date_of_finish',
            'active',
            'watch',
            'images',
            'comments'
        )


class CategorySerializer(serializers.ModelSerializer):
    discounts = DiscountsSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name', 'image', 'slug','discounts')

class AnotherPhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnotherPhones
        fields = ("__all__")

class FelialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Felials
        fields = ("__all__")

class PartnerSerializer(serializers.ModelSerializer):
    discounts = DiscountsSerializer(many=True, read_only=True)  # Ссылка на все элементы связанных моделей
    felials = FelialsSerializer(many=True, read_only=True)  # Ссылка на все элементы связанных моделей
    another_phones = AnotherPhonesSerializer(many=True, read_only=True)  # Ссылка на все элементы связанных моделей
    class Meta:
        model = Partner
        fields = ('owner',
                  'name',
                  'inn',
                  'contact_face',
                  'phone',
                  'adress',
                  'email',
                  'logo',
                  'link',
                  'instagram',
                  'facebook',
                  'linkedin',
                  'active',
                  'date_of_create',
                  'discounts',
                  'felials',
                  'another_phones'
                  )
"""
class DiscountsSerializer(serializers.Serializer):
    partner = serializers.PrimaryKeyRelatedField(queryset = Partner.objects.all())
    name = serializers.CharField(max_length=255)
    body = serializers.CharField()
    discount = serializers.IntegerField()
    slug = serializers.SlugField()
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    date_of_create = serializers.DateTimeField(default = default_datetime())
    date_of_finish = serializers.DateTimeField()
    active = serializers.BooleanField(default=False)
    watch = serializers.IntegerField()

    def create(self, validated_data):
        return Discounts.objects.create(**validated_data)
"""

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("__all__")

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("__all__")

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ("__all__")

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("__all__")
