from django.shortcuts import render

from .models import Business, NeighbourHood, User

# Create your views here.
def home(request):

    return render(request, 'home.html')

def business(request):
    business_list=Business.objects.all()
    context={'business_list': business_list}
    return render(request, 'business.html', context)

def wines(request):
    return render(request, 'wines.html')
def mixed(request):
    return render(request, 'mixed.html')
