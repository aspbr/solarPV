from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer, TestSequenceSerializer, TestStandardSerializer, ClientSerializer, LocationSerializer
from .models import Product, Location, Client, TestStandard, TestSequence

# Create your views here.
@api_view(['GET'])
def productOverview(request):
    product_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>'
    }

    return Response(product_urls)

@api_view(['GET'])
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    product.delete()
        
    return Response('Items delete complete.')


@api_view(['GET'])
def showAllLocations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewLocation(request, pk):
    location = Location.objects.get(location_id=pk)
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createLocation(request):
    serializer = LocationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateLocation(request, pk):
    location = Location.objects.get(location_id=pk)
    serializer = LocationSerializer(location, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def deleteLocation(request, pk):
    location = Location.objects.get(location_id=pk)
    location.delete()
        
    return Response('Items delete complete.')



@api_view(['GET'])
def showAllClients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewClient(request, pk):
    client = Client.objects.get(client_id=pk)
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createClient(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateClient(request, pk):
    client = Client.objects.get(client_id=pk)
    serializer = ClientSerializer(client, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def deleteClient(request, pk):
    client = Client.objects.get(client_id=pk)
    client.delete()
        
    return Response('Items delete complete.')




@api_view(['GET'])
def showAllTestStandards(request):
    testStandards = TestStandard.objects.all()
    serializer = TestStandardSerializer(testStandards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewTestStandard(request, pk):
    testStandard = TestStandard.objects.get(test_standard_id=pk)
    serializer = TestStandardSerializer(testStandard, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTestStandard(request):
    serializer = TestStandardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateTestStandard(request, pk):
    testStandard = TestStandard.objects.get(test_standard_id=pk)
    serializer = TestStandardSerializer(testStandard, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def deleteTestStandard(request, pk):
    testStandard = TestStandard.objects.get(test_standard_id=pk)
    testStandard.delete()
        
    return Response('Items delete complete.')



@api_view(['GET'])
def showAllTestSequences(request):
    testSequences = TestSequence.objects.all()
    serializer = TestSequenceSerializer(testSequences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewTestSequence(request, pk):
    testSequence = TestSequence.objects.get(test_standard_id=pk)
    serializer = TestSequenceSerializer(testSequence, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTestSequence(request):
    serializer = TestSequenceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateTestSequence(request, pk):
    testSequence = TestSequence.objects.get(test_standard_id=pk)
    serializer = TestSequenceSerializer(testSequence, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def deleteTestSequence(request, pk):
    testSequence = TestSequence.objects.get(test_standard_id=pk)
    testSequence.delete()
        
    return Response('Items delete complete.')