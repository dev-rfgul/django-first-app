from django.http  import HttpResponse
from django.shortcuts import render



def home(request):
    # return HttpResponse("Hello World, you are at home")
    return render(request, 'index.html')
    
def about(request):
    # return HttpResponse("Hello World, you are at about")
    return render(request, 'about.html')
def contact(request):
    # return HttpResponse("Hello World, you are at contact ")
    return render(request,'contact.html')
