from django.db import models

# Create your models here.

class AirCompany(models.Model):
    name = models.CharField(max_length=30)
    exp = models.IntegerField()


class Airplane(models.Model):
    name = models.CharField(max_length=30)
    aircompany = models.ForeignKey(AirCompany, on_delete=models.CASCADE, null=True)    
    
