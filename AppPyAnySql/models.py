from django.db import models

# Create your models here.
class Datos(models.Model):
    Description = models.CharField(max_length=500)
    Num = models.FloatField()
