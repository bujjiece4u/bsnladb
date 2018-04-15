from django.http import HttpResponse

from .models import bsnlsitedb

#def index(request):
#    return HttpResponse("Welcome to BSNL site for entry form.")
def index(request):
    latest_bsnlsitedb_list = bsnlsitedb.objects.all()
    output = ', '.join([q.sitename for q in latest_bsnlsitedb_list])
    return HttpResponse(output)


def detail(request, bsnlsitedb_id):
    return HttpResponse("You're looking at question %s." % bsnlsitedb_id)

def results(request, bsnlsitedb_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % bsnlsitedb_id)

def entry(request, bsnlsitedb_id):
    return HttpResponse("You're voting on question %s." % bsnlsite_db)
