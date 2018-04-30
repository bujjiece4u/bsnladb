from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^table/$', views.index, name='index'),
    # ex: /bsnlsite/5/
    path('<int:bsnlsitedb_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:bsnlsitedb_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:bsnlsitedb_id>/entry/', views.entry, name='entry'),

    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^list/$', views.output_table, name='output_table'),
    url(r'^search/', include('haystack.urls')),
    # url(r'^search/(?P<search_term>[\w-]+)/$', views.index, name='index'),
]
