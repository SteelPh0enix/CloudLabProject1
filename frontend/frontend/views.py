from django import template
from django.shortcuts import render
from os import environ

def fibo_calc(request):
    return render(request, 'fibo.html', {'backend_host': environ['BACKEND_HOST'], 'backend_port': environ['BACKEND_PORT']})

def docs(request):
    return render(request, 'README.html')

def home(request):
    return render(request, 'index.html')