from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()
    context = {
        'dojos' : dojos,
        'ninjas': ninjas
    }
    return render(request,'index.html',context)

def dojo_add(request):
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        city_from_form = request.POST.get('city')
        state_from_form = request.POST.get('state')
        Dojo.objects.create(name = name_from_form, city = city_from_form , state = state_from_form)
        return redirect('/')
    return render(request,'index.html')
def ninja_add(request):
    if request.method == "POST":
        first_name_from_form = request.POST.get('first_name')
        last_name_from_form = request.POST.get('last_name')
        id_from_form = request.POST.get('dojo')
        Ninja.objects.create(first_name = first_name_from_form, last_name = last_name_from_form , dojo = Dojo.objects.get(id = id_from_form ))
        return redirect('/')
    return render(request,'index.html')
