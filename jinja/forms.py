from django import forms 
from .models import ChaiVariety 


class chaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label='Chai Variety')
