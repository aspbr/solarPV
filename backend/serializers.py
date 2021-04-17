from rest_framework import serializers
from .models import Product, Location, Client, TestStandard, TestSequence

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class TestStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStandard
        fields = '__all__'

class TestSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSequence
        fields = '__all__'