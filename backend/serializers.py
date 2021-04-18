from rest_framework import serializers
from .models import Product, Location, Client, TestStandard, TestSequence, Service, PerformanceData, User, Certificate

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

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PerformanceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceData
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'