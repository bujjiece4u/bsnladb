from django.db import models

# Create your models here.
class bsnlsitedb(models.Model):
    sitename = models.CharField(max_length=200)
    btstype  = models.CharField(max_length=8)
    btsmake  = models.CharField(max_length=200)
    battery  = models.CharField(max_length=5)
    powerplant = models.CharField(max_length=4)
    ac         = models.CharField(max_length=2)
