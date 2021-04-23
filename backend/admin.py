from django.contrib import admin
from . models import Product, Location, Client, TestStandard, TestSequence, Service, PerformanceData, User, Certificate

class CertificateAdmin(admin.ModelAdmin):
    fields = ('user', 'product')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code')

class UserAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'email', 'job_title')
    search_fields = ['first_name', 'last_name'] 

class PerformanceDataAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('product', 'test_sequence', 'description', 'max_system_voltage')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('voc', 'isc', 'vmp', 'imp', 'pmp', 'ff'),
        }),
    )

# Register your models here.
admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Location)
admin.site.register(TestStandard)
admin.site.register(TestSequence)
admin.site.register(Service)
admin.site.register(PerformanceData, PerformanceDataAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Certificate, CertificateAdmin)