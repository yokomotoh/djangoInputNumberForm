from datetime import datetime
from pyexpat import model

from django.forms import formset_factory
from django.shortcuts import render
from django.views import View

from .forms import CreateNewList, InputNumberForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, TestNumberModel, pim

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
    fields = [
        'test_number_name',
        'test_number',
        'test_number_one',
        'test_number_two',
    ]

    def get_success_url(self):
        #return reverse('testnumber-detail', kwargs={'pk': self.kwargs['pk']})
        return reverse('testnumber-list')


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
        "test_number_name",
        "test_number",
        "test_number_one",
        "test_number_two",
    ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    #success_url = reverse_lazy('testnumber-list') #'/'
    #success_url = reverse_lazy('testnumber-detail', args=(model.pk)) <-???

    def get_success_url(self):
        #return reverse('testnumber-detail', kwargs={'pk': self.kwargs['pk']})
        return reverse('testnumber-calcul', kwargs={'pk': self.kwargs['pk']})

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(TestNumberModel, id = id)

    # pass the object as instance in form
    form = InputNumberForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "testnumbermodel_update.html", context)


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

    ### pickle
    num_new_model = new_model.objects.count()
    latest_new_model_result_test_number = new_model.objects.all()[num_new_model - 1].args.result_test_number
    latest_new_model_result_number = new_model.objects.all()[num_new_model - 1].args.result_number
    latest_new_model_test_result = new_model.objects.all()[num_new_model - 1].args.test_result
    #test_time = datetime.now()#new_model.objects.all()[num_new_model - 1].args.test_result['40']['time_result_calcul']

    context = {
        'num_testnumber': num_testnumber,
        'num_greater_than_twenty_testnumber': num_gr_twenty_testnumber,
        'num_visits': num_visits,
        'latest_new_model_result_test_number': latest_new_model_result_test_number,
        'latest_new_model_result_number': latest_new_model_result_number,
        'latest_new_model_test_result': latest_new_model_test_result,
        #'test_time': test_time
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views.generic.edit import FormView
from .forms import InputNumberForm
class InputFormCalculView(UpdateView):
#class InputFormCalculView(FormView):
    model = TestNumberModel
    fields = [
        "test_number_name",
        "test_number",
        "test_number_one",
        "test_number_two",
    ]

    #form_class = InputNumberForm

    template_name = "numberform/testnumbermodel_calcul.html"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        print(form.cleaned_data)
        return super().form_valid(form)

    # can specify success url
    # url to redirect after successfully
    # updating details
    #success_url = reverse_lazy('testnumber-list') #'/'

    def get_success_url(self):
        #return reverse('testnumber-detail', kwargs={'pk': self.kwargs['pk']})
        return reverse('testnumber-list')

##### model view for picke

from .models import new_model
class NewModelList(ListView):
    model = new_model
