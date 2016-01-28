from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    html = '<body><h1>Hello Heroku!!!</h1></body>'
    return HttpResponse(html)