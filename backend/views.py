from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import ProductSerializer, TestSequenceSerializer, TestStandardSerializer, ClientSerializer, LocationSerializer, CertificateSerializer, ServiceSerializer
from .models import Product, Location, Client, TestStandard, TestSequence, Service, Certificate

from rest_framework import permissions

# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
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
@permission_classes((permissions.AllowAny,))
def showAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def viewProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteProduct(request, pk):
    product = Product.objects.get(product_id=pk)
    product.delete()
        
    return Response('Items delete complete.')


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def showAllLocations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def viewLocation(request, pk):
    location = Location.objects.get(location_id=pk)
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createLocation(request):
    serializer = LocationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updateLocation(request, pk):
    location = Location.objects.get(location_id=pk)
    serializer = LocationSerializer(location, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteLocation(request, pk):
    location = Location.objects.get(location_id=pk)
    location.delete()
        
    return Response('Items delete complete.')



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def showAllClients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def viewClient(request, pk):
    client = Client.objects.get(client_id=pk)
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createClient(request):
    serializer = ClientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updateClient(request, pk):
    client = Client.objects.get(client_id=pk)
    serializer = ClientSerializer(client, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteClient(request, pk):
    client = Client.objects.get(client_id=pk)
    client.delete()
        
    return Response('Items delete complete.')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def showAllTestStandards(request):
    testStandards = TestStandard.objects.all()
    serializer = TestStandardSerializer(testStandards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def viewTestStandard(request, pk):
    testStandard = TestStandard.objects.get(test_standard_id=pk)
    serializer = TestStandardSerializer(testStandard, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createTestStandard(request):
    serializer = TestStandardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updateTestStandard(request, pk):
    testStandard = TestStandard.objects.get(test_standard_id=pk)
    serializer = TestStandardSerializer(testStandard, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteTestStandard(request, pk):
    testStandard = TestStandard.objects.get(test_standard_id=pk)
    testStandard.delete()
        
    return Response('Items delete complete.')


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def showAllTestSequences(request):
    testSequences = TestSequence.objects.all()
    serializer = TestSequenceSerializer(testSequences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def viewTestSequence(request, pk):
    testSequence = TestSequence.objects.get(test_standard_id=pk)
    serializer = TestSequenceSerializer(testSequence, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createTestSequence(request):
    serializer = TestSequenceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateTestSequence(request, pk):
    testSequence = TestSequence.objects.get(test_standard_id=pk)
    serializer = TestSequenceSerializer(testSequence, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteTestSequence(request, pk):
    testSequence = TestSequence.objects.get(test_standard_id=pk)
    testSequence.delete()
        
    return Response('Items delete complete.')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def showAllServices(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def viewService(request, pk):
    service = Service.objects.get(id=pk)
    serializer = ServiceSerializer(service, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createService(request):
    serializer = ServiceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateService(request, pk):
    service = Service.objects.get(id=pk)
    serializer = ServiceSerializer(service, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteService(request, pk):
    service = Service.objects.get(id=pk)
    service.delete()
        
    return Response('Items delete complete.')


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def showAllCertificates(request):
    certificates = Certificate.objects.all()
    serializer = CertificateSerializer(certificates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def viewCertificate(request, pk):
    certificate = Certificate.objects.get(id=pk)
    serializer = CertificateSerializer(certificate, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createCertificate(request):
    serializer = CertificateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateCertificate(request, pk):
    certificate = Certificate.objects.get(id=pk)
    serializer = CertificateSerializer(certificate, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteCertificate(request, pk):
    certificate = Certificate.objects.get(id=pk)
    certificate.delete()
        
    return Response('Items delete complete.')