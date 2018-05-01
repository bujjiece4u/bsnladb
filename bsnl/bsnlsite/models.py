from django.db import models
from django.forms import ModelForm
from haystack import indexes

# Create your models here.
BTSTYPE_CHOICES = (
('2g', '2G'),
('3g', '3G'),
('2g+3g', '2G+3G'),
('te', 'TE'),
('te+2g', 'TE+2G'),
('te+2g+3g', 'TE+2G+3G'),

)

BATTERYTYPE_CHOICES =(
('100ah', '100AH'),
('200ah', '200AH'),
('300ah', '300AH'),
)
POWERPLANTMODULE_CHOICES = (
('50a', '50A'),
('10a', '10A'),
('25a', '25A'),
('100a', '100A'),
)

ACCAPACITY_CHOICES =(
('1t', '1T'),
('1.5t', '1.5T'),
('2t', '2T'),
('2.5t', '2.5T'),

)
class bsnlsitedb(models.Model):
    sitename = models.CharField(max_length=200,unique=True)
    btstype  = models.CharField(max_length=8,choices=BTSTYPE_CHOICES,default='2G')
    btsmake  = models.CharField(max_length=200)
    battery  = models.CharField(max_length=200)
    batterytype = models.CharField(max_length=5,choices=BATTERYTYPE_CHOICES,default='100AH')
    powerplant = models.CharField(max_length=200)
    powerplantmodule = models.CharField(max_length=4, choices=POWERPLANTMODULE_CHOICES,default='50A')
    ac1make         = models.CharField(max_length=200)
    ac1capacity         = models.CharField(max_length=4,choices=ACCAPACITY_CHOICES,default='1T')
    ac2make         = models.CharField(max_length=200)
    ac2capacity         = models.CharField(max_length=4,choices=ACCAPACITY_CHOICES,default='1T')
    ac3make         = models.CharField(max_length=200)
    ac3capacity         = models.CharField(max_length=4,choices=ACCAPACITY_CHOICES,default='1T')
    ac4make         = models.CharField(max_length=200)
    ac4capacity         = models.CharField(max_length=4,choices=ACCAPACITY_CHOICES,default='1T')
    ac5make         = models.CharField(max_length=200)
    ac5capacity         = models.CharField(max_length=4,choices=ACCAPACITY_CHOICES,default='1T')


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    sitename = indexes.CharField(model_attr='sitename')
    btsmake = indexes.CharField(model_attr='btsmake')

# class My_Model_Form(ModelForm):
#            class Meta:
#                model = bsnlsitedb

class bsnlsitedbIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    sitename = indexes.CharField(model_attr='sitename')
    btstype = indexes.CharField(model_attr='btstype')

    def get_model(self):
        return bsnlsitedb
