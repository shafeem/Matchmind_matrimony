from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from main.models import Account
from main.views import home

# Create your views here.


def userlogin(request):
    # if request.user.is_authenticated:
    #    return redirect('homePage.html') 

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            
            login(request,user)
            return redirect(home)
           
        
        else:
            messages.info(request,'enter a valid username or password')
    return render(request,'login.html')


def index(request):
    return render(request,'adminPage.html')

def loginPage(request):
    return render(request,'login.html')