from django.shortcuts import render
from catalog.models import Architect, Contractor, Consumer, Plan, Element
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View

import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import EditPlanForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from catalog.forms import EditPlanForm

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_contractors = Contractor.objects.all().count()
    num_consumers = Consumer.objects.all().count()
    num_plans = Plan.objects.all().count()

    # approved form factors
    num_approved_plans = Plan.objects.filter(approved__exact=True).count()
    
    # The 'all()' is implied by default.    
    num_architects = Architect.objects.count()
    
    context = {
        'num_contractors': num_contractors,
        'num_consumers': num_consumers,
        'num_plans': num_plans,
        'num_approved_plans': num_approved_plans,
        'num_architects': num_architects,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PlansListView(generic.ListView):
    model = Plan
    paginate_by = 10

class ApprovedPlansListView(generic.ListView):
    model = Plan
    paginate_by = 10
    context_object_name = 'approved_plans_list'   # your own name for the list as a template variable
    queryset = Plan.objects.filter(approved__exact=True)
    template_name = 'catalog/approved_plans_list.html'  # Specify your own template name/location

class PlanDetailView(generic.DetailView):
    model = Plan
    fields = '__all__'

class ArchitectDetailView(generic.DetailView):
    model = Architect


class PlansApplyedByConsumerListView(LoginRequiredMixin, generic.ListView, PermissionRequiredMixin, View):
    """Generic class-based view listing plans which applyed by current consumer."""
    permission_required = 'catalog.can_apply_plan'
    model = Plan
    template_name ='catalog/plans_list_applyed_by_consumer.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Plan.objects.filter(consumer=self.request.user).filter(approved__exact=True).order_by('apply_date')

class ArchitectManagePlans(LoginRequiredMixin, generic.ListView, PermissionRequiredMixin, View):
    """Create plan by architect."""
    permission_required = 'catalog.can_create_plan'
    model = Plan
    template_name ='catalog/architect_plans_management.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Plan.objects.filter(architect=self.request.user).filter(architect=self.request.user).order_by('creation_date')

class PlanCreate(CreateView):
    model = Plan
    #fields = ['name']
    fields = '__all__'
    initial = {'name': 'My new plan'}

class PlanUpdate(UpdateView):
    model = Plan
    #fields = ['name']
    fields = '__all__'

class PlanDelete(DeleteView):
    model = Plan
    success_url = reverse_lazy('plans')

@permission_required('catalog.can_edit_plan')
def edit_plan_architect(request, pk):
    """View function for editing plan by architect."""
    a = 'aaaaaa'
    b = 'd'
    plan = get_object_or_404(Plan, pk=pk)
    #element = get_object_or_404(Element, pk=plan.id)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = EditPlanForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            plan.name = form.cleaned_data['name']
            plan.save()

            # redirect to a new URL:
           # return HttpResponseRedirect("" )
            
    # If this is a GET (or any other method) create the default form.
    else:
        name = 'New plan'
        form = EditPlanForm(initial={'name': name})

    context = {
        'form': form,
        'plan': plan,
        'a': a,
        'b': b,
    }

    return render(request, 'catalog/edit_plan_architect.html', context)

def save_events_json(request):
    if request.is_ajax():
        if request.method == 'POST':
            print 'Raw Data: "%s"' % request.body   
    return HttpResponse("OK")