from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'esportsplatform_main/index.html')

def competition_registration(request):
    return render(request, 'esportsplatform_main/competition_registration.html')