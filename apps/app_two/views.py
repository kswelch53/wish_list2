from django.shortcuts import render, HttpResponse, redirect
from .models import Items

# Create your views here.
def index(request):
    response = "Hello, I am your second request!"
    print("I am views.py")
    return HttpResponse(response)
