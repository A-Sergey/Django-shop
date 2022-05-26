#from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

def about_us(request):
    context = {'form':AuthenticationForm(),}
    return render(request,'about_us.html',context)
