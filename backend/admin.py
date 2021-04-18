from django.contrib import admin
from . models import Product, Location, Client, TestStandard, TestSequence, Service, PerformanceData, User, Certificate

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(TestStandard)
admin.site.register(TestSequence)
admin.site.register(Service)
admin.site.register(PerformanceData)
admin.site.register(User)
admin.site.register(Certificate)