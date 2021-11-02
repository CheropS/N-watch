from django.shortcuts import render

from .models import Business
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):

    return render(request, 'home.html')

def business(request):
    business_list=Business.objects.all()
    context={'business_list': business_list}
    return render(request, 'business.html', context)

def add(request):
    return render(request, 'add.html')
    
def about(request):
    return render(request, 'about.html')
