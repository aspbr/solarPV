from django.db import models

# Create your models here.
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, default='SOME STRING')
    author = models.CharField(max_length=100, default='SOME STRING')
    email = models.EmailField(max_length=100, default='SOME STRING')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
