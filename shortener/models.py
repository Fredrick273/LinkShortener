from django.db import models

# Create your models here.
class ShortenUrl(models.Model):
    link = models.CharField(max_length=200)
    name = models.CharField(max_length=10,null=True)
    code =  models.CharField(max_length=10,unique=True)