from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /bsnlsite/5/
    path('<int:bsnlsitedb_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:bsnlsitedb_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:bsnlsitedb_id>/entry/', views.entry, name='entry'),    
]
