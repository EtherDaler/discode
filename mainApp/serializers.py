from rest_framework import serializers

class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = ('id', 'partner', 'name', 'body', 'discount', 'slug', 'categorys', 'date_of_create', 'date_of_finish', 'active', 'watch')