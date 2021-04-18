from django.urls import path
from . import views

urlpatterns = [
    path('', views.productOverview, name='productOverview'),
    
    path('product-list/', views.showAll, name='product-list'),
    path('product-detail/<int:pk>/', views.viewProduct, name='product-detail'),
    path('product-create/', views.createProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),

    path('location-list/', views.showAllLocations, name='location-list'),
    path('location-detail/<int:pk>/', views.viewLocation, name='location-detail'),
    path('location-create/', views.createLocation, name='location-create'),
    path('location-update/<int:pk>/', views.updateLocation, name='location-update'),
    path('location-delete/<int:pk>/', views.deleteLocation, name='location-delete'),

    path('test-standard-list/', views.showAllTestStandards, name='test-standard-list'),
    path('test-standard-detail/<int:pk>/', views.viewTestStandard, name='test-standard-detail'),
    path('test-standard-create/', views.createTestStandard, name='test-standard-create'),
    path('test-standard-update/<int:pk>/', views.updateTestStandard, name='test-standard-update'),
    path('test-standard-delete/<int:pk>/', views.deleteTestStandard, name='test-standard-delete'),

    path('test-sequence-list/', views.showAllTestSequences, name='test-sequence-list'),
    path('test-sequence-detail/<int:pk>/', views.viewTestSequence, name='test-sequence-detail'),
    path('test-sequence-create/', views.createTestSequence, name='test-sequence-create'),
    path('test-sequence-update/<int:pk>/', views.updateTestSequence, name='test-sequence-update'),
    path('test-sequence-delete/<int:pk>/', views.deleteTestSequence, name='test-sequence-delete'),
]