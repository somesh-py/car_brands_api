from rest_framework import serializers
from .models import Car

class CarSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    company=serializers.CharField(max_length=100)
    cost=serializers.CharField(max_length=100)
    color=serializers.CharField(max_length=100)
    ratings=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
