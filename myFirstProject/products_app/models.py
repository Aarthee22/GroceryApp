from django.db import models

# Create your models here.
class OrderList(models.Model):
    username=models.CharField(max_length=100)
    wholeList=models.CharField(max_length=500,blank=True,null=True)