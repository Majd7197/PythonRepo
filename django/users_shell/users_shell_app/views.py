from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse('HELLO WORLD')

# Create your views here.
