from rest_framework import serializers
from inventory.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'shelf_id', 'reference', 'good_thru', 'observation')