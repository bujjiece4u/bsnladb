from django.http import HttpResponse
from django.template import loader
from haystack import indexes
from .models import bsnlsitedb
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .forms import PostForm
from django.shortcuts import render_to_response
import operator
from django.views.generic import ListView
from django.views.generic.list import BaseListView

from django.db.models import Q
# from .models import BlogSearchListView

def home(request):
    template = loader.get_template('bsnlsite/home.html')
    return HttpResponse(template.render())
    #    return HttpResponse("Welcome to BSNL site for entry form.")
def index(request,search_term=None):
    latest_bsnlsitedb_list = bsnlsitedb.objects.all()
    template = loader.get_template('bsnlsite/index.html')
    context = {
        'latest_bsnlsitedb_list': latest_bsnlsitedb_list,
    }
    return HttpResponse(template.render(context, request))
#    output = ', '.join([q.sitename for q in latest_bsnlsitedb_list])
#    return HttpResponse(output)


def detail(request, bsnlsitedb_id):
    return HttpResponse("You're looking at database %s." % bsnlsitedb_id)

def results(request, question_id):
    question = get_object_or_404(bsnlsitedb, pk=question_id)
    return render(request, 'bsnlsite/results.html', {'question': question})
# def results(request, bsnlsitedb_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % bsnlsitedb_id)

#...
def entry(request, bsnlsitedb_id):
    question = get_object_or_404(bsnlsitedb, pk=bsnlsitedb_id)
    try:
        selected_choice = question.sitename
    except (KeyError, sitename.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'bsnlsite/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bsnlsite:results', args=(question.id,)))
#            return HttpResponse("You're voting on question %s." % bsnlsite_db)

def post_new(request):
    # instance = get_object_or_404(bsnlsitedb, bsnlsitedb_id=id)
    # form = PostForm(request.POST or None, instance=instance)
    # if form.is_valid():
    #     form.save()
    #     return redirect('next_view')
    # args = {}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
            success = True
            print("form accepted")
        else:
            print(form.errors)
    else:
        form = PostForm()
        # args['form'] = form
    return render(request, 'bsnlsite/post_edit.html', {'form': form})

def output_table(request):
    output = bsnlsitedb.objects.all()
    return render_to_response('bsnlsite/outputtable.html', {'output': output})

# class BlogSearchListView(BlogListView):
#     """
#     Display a Blog List page filtered by the search query.
#     """
#     paginate_by = 10



def get_queryset(self):
        # results = bsnlsitedb.objects.filter(Q(sitename__icontains=your_search_query) | Q(intro__icontains=your_search_query) | Q(content__icontains=your_search_query))

        result = super(BlogSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (bsnlsitedb(sitename__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (bsnlsitedb(btstype__icontains=q) for q in query_list))
            )

        return render(result, 'bsnlsite/search.html')

    # return render(request, 'bsnlsite/post_edit.html', {'form': form})





    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

def search(request):
    form = ItemSearchForm(request.GET)
    results = form.search()
    return render(request, 'search/search.html', {
        'items': results
    })
