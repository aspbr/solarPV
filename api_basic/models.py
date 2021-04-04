from django.db import models

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