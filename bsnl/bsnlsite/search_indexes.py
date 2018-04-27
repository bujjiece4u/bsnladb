import datetime
from haystack import indexes
from .models import bsnlsitedb


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    sitename = indexes.CharField(model_attr='sitename')
    btstype = indexes.DateTimeField(model_attr='btstype')

    def get_model(self):
        return bsnlsitedb

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
