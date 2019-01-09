from django.shortcuts import render
from catalog.models import Author, CompanyUser, PrivateUser, FormFactor

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_company_users = CompanyUser.objects.all().count()
    num_private_users = PrivateUser.objects.all().count()
    num_form_factors = FormFactor.objects.all().count()

    # finalised form factors
    num_finalize_form_factors = FormFactor.objects.filter(finalized__exact=True).count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_company_users': num_company_users,
        'num_private_users': num_private_users,
        'num_form_factors': num_form_factors,
        'num_finalize_form_factors': num_finalize_form_factors,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
