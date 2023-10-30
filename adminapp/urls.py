from django.urls import path
from . import views

urlpatterns = [
    path('loginPage/',views.userlogin,name='userlogin'),
    path('index/',views.index,name='index')
]