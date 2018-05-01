from django import forms
from haystack.forms import SearchForm

from .models import bsnlsitedb

class PostForm(forms.ModelForm):

    class Meta:
        model = bsnlsitedb
        fields = ('sitename',
                  'btstype',
                  'btsmake',
                  'battery',
                  'batterytype',
                  'powerplant',
                  'powerplantmodule',
                  'ac1make',
                  'ac1capacity',
                  'ac2make',
                  'ac2capacity',
                  'ac3make',
                  'ac3capacity',
                  'ac4make',
                  'ac4capacity',
                  'ac5make',
                  'ac5capacity',
                  )

class ItemSearchForm(SearchForm):
    def search(self):
        sqs = super(ItemSearchForm, self).search().models(bsnlsitedb)
        return sqs
