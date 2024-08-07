from django.shortcuts import render,HttpResponse,redirect
from .models import Dojo,Ninja
def index(request):
    context = {
        "dojos": Dojo.objects.all() ,
        "ninjas": Ninja.objects.all()
    }
    return render(request,'index.html',context)

def dojo_add(request):
    if request.method == "POST":
        name_from_form = request.POST['name']
        city_from_form = request.POST['city']
        state_from_form = request.POST['state']
        Dojo.objects.create(name=name_from_form, city=city_from_form, state=state_from_form)
        return redirect("/")
def ninja_add(request):
    if request.method == "POST":
        first_name_from_form = request.POST['first_name']
        last_name_from_form = request.POST['last_name']
        dojo_id_from_form = request.POST.get('dojo')
        dojo_instance = Dojo.objects.get(id=dojo_id_from_form)
        Ninja.objects.create(first_name=first_name_from_form, last_name=last_name_from_form, dojo=dojo_instance)
        return redirect("/")
