from pyexpat import model

from django.forms import formset_factory
from django.shortcuts import render
from .forms import CreateNewList
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, TestNumberModel


# Create your views here.
'''
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "numberform/list.html", {"ls":ls})

def home(response):
    return render(response, "numberform/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "numberform/create.html", {"form": form})
'''
'''
from .forms import InputForm

def home_view(request):
    #model = TestNumberModel

    #context = {}

    ##homeFormSet = formset_factory(TestNumberModel)
    ##formset = homeFormSet()

    #context['form']= InputForm()
    ##create['formset'] = formset
    #return render(request, "numberform/inputform.html", context)
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')

from django.views import View

class HomeView(View):

    def get(self, request):
        num_numbers = TestNumberModel.objects.all().count()
        # <view logic>
        return HttpResponse('result')

'''
from django.views.generic.edit import CreateView
class InputFormCreate(CreateView):
    model = TestNumberModel
    fields = ['test_number']

from django.views.generic.list import ListView
class InputFormList(ListView):
    model = TestNumberModel

from django.views.generic.detail import DetailView
class InputFormDetailView(DetailView):
    model = TestNumberModel

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse


class InputFormUpdateView(UpdateView):
    model = TestNumberModel
    fields = [
        "test_number",
    ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    #success_url = reverse_lazy('testnumber-list') #'/'
    #success_url = reverse_lazy('testnumber-detail', args=(model.pk)) <-???

    def get_success_url(self):
        return reverse('testnumber-detail', kwargs={'pk': self.kwargs['pk']})

from django.views.generic.edit import DeleteView
class InputFormDeleteView(DeleteView):
    model = TestNumberModel
    success_url = reverse_lazy('testnumber-list')


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_testnumber = TestNumberModel.objects.all().count()
    num_gr_twenty_testnumber = TestNumberModel.objects.filter(test_number__gt=20).count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_testnumber': num_testnumber,
        'num_greater_than_twenty_testnumber': num_gr_twenty_testnumber,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
