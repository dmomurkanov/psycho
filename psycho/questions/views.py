from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> AAAA </h1>")