from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home.html')

def business(request):
    return render(request, 'business.html')

def wines(request):
    return render(request, 'wines.html')
def mixed(request):
    return render(request, 'mixed.html')
