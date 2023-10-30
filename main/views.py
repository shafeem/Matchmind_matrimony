from django.shortcuts import render
from .models import PersonalityTypes

# Create your views here.


def home(request):
    return render(request,'HomePage.html')


def personalityType(request):
   
    allTypes=PersonalityTypes.objects.all()
    return render(request,'PersonalityTypes.html',{'alltypes':allTypes})

def personalityTest(request):
    output_set={}
    questin_dict={
        'Do you generally prefer to socialize in large groups rather than one-on-one or small gatherings':'Do you generally prefer to socialize in large groups rather than one-on-one or small gatherings',
        'b':'b',
        'c':'c',
        'd':'d',

    }

    

    return render(request,'PersonalityTest.html',{'questin_dict':questin_dict})



def AllProfiles(request):
    return render(request,'all-profiles.html')

def aboutpage(request):
    return render(request,'about.html')