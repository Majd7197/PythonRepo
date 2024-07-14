from django.shortcuts import render, redirect,HttpResponse
from .models import User

def index(request):
    context = {
        "users": User.objects.all() 
    }
    return render(request, 'index.html', context)

def add_user(request):
    if request.method == "POST":
        first_name_from_form = request.POST['first_name']
        last_name_from_form = request.POST['last_name']
        email_from_form = request.POST['email']
        age_from_form = request.POST['age']
        User.objects.create(first_name=first_name_from_form, last_name=last_name_from_form, email=email_from_form, age=age_from_form)
        return redirect("/")
    return HttpResponse("Invalid method", status=405)
