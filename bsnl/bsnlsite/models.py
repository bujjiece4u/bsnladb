from django.db import models

# Create your models here.
BTSTYPE_CHOICES = (
('2g', '2G'),
('3g', '3G'),
('2g+3g', '2G+3G'),
('te', 'TE'),
('te+2g', 'TE+2G'),
('te+2g+3g', 'TE+2G+3G'),

)
class bsnlsitedb(models.Model):
    sitename = models.CharField(max_length=200)
    btstype  = models.CharField(max_length=8,choices=BTSTYPE_CHOICES,default='2G')
    btsmake  = models.CharField(max_length=200)
    battery  = models.CharField(max_length=5)
    powerplant = models.CharField(max_length=4)
    ac         = models.CharField(max_length=2)
