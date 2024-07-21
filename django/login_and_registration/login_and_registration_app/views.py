from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request,'index.html')
        else:
            first_name_from_form = request.POST.get('first_name')
            last_name_from_form = request.POST.get('last_name')
            email_from_form = request.POST.get('email')
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            request.session['first_name']= first_name_from_form
            request.session['last_name']= last_name_from_form
            request.session['email'] = email_from_form
            print(pw_hash)        
            User.objects.create(first_name=first_name_from_form ,last_name = last_name_from_form, email = email_from_form, password = pw_hash)
            return redirect('/')
    return render(request, 'index.html')

