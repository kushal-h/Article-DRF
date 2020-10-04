
from django.db import models

# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    email = models.EmailField(max_length=250)
    date =  models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return  self.title