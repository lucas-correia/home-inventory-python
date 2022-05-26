from rest_framework import serializers
from inventory.models import Shelf

class ShelfSerializer(serializers.ModelSerializer):

    class Meta:
            model = Shelf
            fields = ('id', 'name', 'position')