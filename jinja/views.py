from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
# Create your views here.
def jinja(request):
    chais=ChaiVariety.objects.all()
    return render(request,'jinja/index.html',{'chais':chais})

def chai_details(request,chai_id):
    chai=get_object_or_404(ChaiVariety,pk=chai_id)  
    return render(request,'jinja/chai_details.html',{'chai':chai})