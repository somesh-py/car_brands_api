from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    cost=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    ratings=models.CharField(max_length=100)