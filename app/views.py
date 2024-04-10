from django.shortcuts import render, HttpResponse
from . import helper

# Create your views here.


def home(request):
    helper.make_report(data={})
    return HttpResponse('<h1>I am Home</h1>')
