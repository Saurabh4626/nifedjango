from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

# Create your views here.


def login(request):
    return render(request, 'nifeapp/login.html')


def register(request):
	return render(request, 'nifeapp/register.html')

def deployapplication(request):
    return render(request, 'nifeapp/deployapplication.html')
