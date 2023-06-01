from django.db import models
from django.core.exceptions import FieldDoesNotExist


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    department= models.CharField(max_length=64)
    email = models.CharField(max_length=128,null=True)
    active = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
# Create your models here.

class Applicant(models.Model):
    applicant_number = models.CharField(max_length=5)    
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, null=True, default=None)
    phone = models.CharField(max_length=12)
    cv = models.FileField(null=True)
    
    def __str__(self):
        return self.name


    