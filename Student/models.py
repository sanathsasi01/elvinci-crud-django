import email
from statistics import mode
from django.db import models

# Create your models here.


class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StudentInstruments(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE, null=True, related_name='instruments', blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
