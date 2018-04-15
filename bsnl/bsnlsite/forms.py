from django import forms

from .models import bsnlsitedb

class PostForm(forms.ModelForm):

    class Meta:
        model = bsnlsitedb
        fields = ('sitename', 'btstype','btsmake',)
