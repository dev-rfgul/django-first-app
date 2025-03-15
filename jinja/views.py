from django.shortcuts import render
from .models import ChaiVariety,store
from django.shortcuts import get_object_or_404
from .forms import chaiVarietyForm


# Create your views here.
def jinja(request):
    chais=ChaiVariety.objects.all()
    return render(request,'jinja/index.html',{'chais':chais})

def chai_details(request,chai_id):
    chai=get_object_or_404(ChaiVariety,pk=chai_id)  
    return render(request,'jinja/chai_details.html',{'chai':chai})

def chai_store_view(request):
    stores=None
    if request.method=='POST':
        form=chaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety=form.cleaned_data['chai_variety']
            stores= store.objects.filter(chai_varities=chai_variety)
    else:
         form=chaiVarietyForm()
    return render(request, 'jinja/chai_stores.html', {'stores': stores, 'form': form})
