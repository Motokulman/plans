from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
    
class EditPlanForm(forms.Form):

    name = forms.CharField(help_text="Enter a name")

    def clean_name(self):
        data = self.cleaned_data['name']
        return data

    x0 = forms.IntegerField(initial = 0)
    y0 = forms.IntegerField(initial = 0)
    x1 = forms.IntegerField(initial = 0)
    y1 = forms.IntegerField(initial = 0)
    
