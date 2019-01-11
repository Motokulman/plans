from django.shortcuts import render
from catalog.models import Author, CompanyUser, PrivateUser, Plan
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_company_users = CompanyUser.objects.all().count()
    num_private_users = PrivateUser.objects.all().count()
    num_plans = Plan.objects.all().count()

    # finalised form factors
    num_finalized_plans = Plan.objects.filter(finalized__exact=True).count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_company_users': num_company_users,
        'num_private_users': num_private_users,
        'num_plans': num_plans,
        'num_finalized_plans': num_finalized_plans,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PlansListView(generic.ListView):
    model = Plan
    paginate_by = 10

class FinalizedPlansListView(generic.ListView):
    model = Plan
    paginate_by = 10
    context_object_name = 'finalized_plans_list'   # your own name for the list as a template variable
    queryset = Plan.objects.filter(finalized__exact=True)
    template_name = 'catalog/finalized_plans_list.html'  # Specify your own template name/location

class PlanDetailView(generic.DetailView):
    model = Plan
    paginate_by = 10

