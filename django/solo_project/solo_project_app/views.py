from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            first_name_from_form = request.POST.get('first_name')
            last_name_from_form = request.POST.get('last_name')
            dob_from_form = request.POST.get('dateofbirth')
            phone_number_from_form = request.POST.get('phone_number')
            email_from_form = request.POST.get('email')
            password = request.POST.get('password')
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)        
            User.objects.create(first_name=first_name_from_form ,last_name = last_name_from_form, email = email_from_form, password = pw_hash, dateofbirth = dob_from_form  , phone_number = phone_number_from_form )
            request.session['first_name'] = request.POST.get('first_name')
            return redirect('/')
    content = {
        'roles': Role.objects.all(),
        'users' : User.objects.all()
    }
    return render(request, 'index.html',content)

def login(request):
    if request.method == "POST":
        users = User.objects.filter(email=request.POST['email'])  
        if users:  
            for user in users:
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['userid'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                    return redirect('/dashboard')
            messages.error(request, "Incorrect Username or password")
        else:
            messages.error(request, "User does not exist")
        return redirect("/")
    return render(request, 'login.html')

