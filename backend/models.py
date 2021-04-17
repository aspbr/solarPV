from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.PositiveIntegerField()
    product_code = models.CharField(max_length=100, default='SOME STRING')
    product_name = models.CharField(max_length=50, default='SOME STRING')
    product_desc = models.CharField(max_length=100, default='SOME STRING')
    specifications = models.CharField(max_length=100, default='SOME STRING')
    manufacturer_id = models.PositiveIntegerField()
    substrate_manufacturer = models.CharField(max_length=50, default='SOME STRING')
    substrate_type = models.CharField(max_length=50, default='SOME STRING')
    superstate_manufacturer = models.CharField(max_length=50, default='SOME STRING')
    superstate_type = models.CharField(max_length=50, default='SOME STRING')
    interconnect_supplier = models.CharField(max_length=50, default='SOME STRING')
    interconnect_material = models.CharField(max_length=50, default='SOME STRING')
    fuse_rating = models.PositiveIntegerField()
    bypass_diodes = models.PositiveIntegerField()
    series_strings = models.PositiveIntegerField()
    cells_series = models.PositiveIntegerField()
    total_cells = models.PositiveIntegerField()
    cell_technology = models.CharField(max_length=50, default='SOME STRING')
    cell_area = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    rated_voc = models.CharField(max_length=100, default='SOME STRING')
    rated_isc = models.CharField(max_length=100, default='SOME STRING')
    rated_vmp = models.CharField(max_length=100, default='SOME STRING')
    rated_imp = models.CharField(max_length=100, default='SOME STRING')
    rated_pmp = models.CharField(max_length=100, default='SOME STRING')
    rated_ff = models.CharField(max_length=100, default='SOME STRING')
    length_str = models.CharField(max_length=30, default='SOME STRING')

    def __str__(self):
        return self.product_name

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=100, default='Client 1')
    client_type = models.CharField(max_length=100, default='Client Type 1')
    
    def __str__(self):
        return self.client_name

# Create your models here.
class Location(models.Model):
    location_id = models.PositiveIntegerField()
    address1 = models.CharField(max_length=100, default='Location Address ')
    address2 = models.CharField(max_length=100, default='SOME STRING')
    city = models.CharField(max_length=100, default='SOME STRING')
    state = models.CharField(max_length=100, default='SOME STRING')
    postal_code = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=50, default='SOME STRING')
    fax_number = models.CharField(max_length=50, default='SOME STRING')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.address1

# Create your models here.
class TestStandard(models.Model):
    standard_name = models.CharField(max_length=100, default='Test Standard 1')
    standard_desc = models.CharField(max_length=100, default='Standard Description')
    published_date = models.DateField()
    
    def __str__(self):
        return self.standard_name

# Create your models here.
class TestSequence(models.Model):
    sequence_name = models.CharField(max_length=100, default='Test Sequence 1')
    
    def __str__(self):
        return self.sequence_name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    author = models.CharField(max_length=100, default='SOME STRING')
    email = models.EmailField(max_length=100, default='SOME STRING')
    date = models.DateTimeField(auto_now_add=True)
    print(author)

    def __str__(self):
        return self.title
        
class A(models.Model):
    def __init__(self, name):
        self.name = name

    #name = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.name


