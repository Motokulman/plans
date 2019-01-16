from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
    
class CreatePlanForm(forms.Form):
    plan_name = forms.CharField(help_text="Enter a name for your new plan")
