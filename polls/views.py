from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hola holita, vecinito')
# Create your views here.
