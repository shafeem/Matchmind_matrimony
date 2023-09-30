from django.shortcuts import render
from .models import PersonalityTypes

# Create your views here.


def home(request):
    return render(request,'HomePage.html')


def personalityTest(request):
   
    allTypes=PersonalityTypes.objects.all()
    return render(request,'PersonalityTypes.html',{'alltypes':allTypes})