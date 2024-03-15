from django.shortcuts import render
from datetime import date


# Create your views here.
def form(request):
    d={'name':'Diksha','data':'hi i am diksha','d':'cat','c':1,'date':date.today()}


    return render(request,'a_cat.html',d)