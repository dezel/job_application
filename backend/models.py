from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    department= models.CharField(max_length=64)
    email = models.CharField(max_length=128,null=True)
    active = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
# Create your models here.
