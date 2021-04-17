from django.contrib import admin
from . models import Product, Location, Client, TestStandard, TestSequence

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(TestStandard)
admin.site.register(TestSequence)