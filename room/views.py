from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render




# Create your views here.
def index(request):
    return HttpResponse('hey')


