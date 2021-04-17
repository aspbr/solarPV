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
class Article(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    author = models.CharField(max_length=100, default='SOME STRING')
    email = models.EmailField(max_length=100, default='SOME STRING')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


