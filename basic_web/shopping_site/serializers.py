from rest_framework import serializers
from shopping_site.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ('id', 'name', 'price', 'status')
