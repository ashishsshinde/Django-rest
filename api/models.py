from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

class Agro(models.Model):
    fromdate = models.CharField(max_length=100)
    todate = models.CharField(max_length=100)
    noofguest = models.CharField(max_length=100)
    typeofacc = models.CharField(max_length=100)
    
    