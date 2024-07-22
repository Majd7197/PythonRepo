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

def login(request):
    if request.method == "POST":
        # See if the email provided exists in the database
        users = User.objects.filter(email=request.POST['email'])  # Using filter

        if users:  # Check if any user was found
            for user in users:
                # Use bcrypt's checkpw method, passing the hash from our database and the password from the form
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    # If we get True after checking the password, we may put the user id in session
                    request.session['userid'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                    # Never render on a post, always redirect!
                    return redirect('/success')
            # If no password matched
            messages.error(request, "Incorrect password")
        else:
            # Handle the case where no users were found
            messages.error(request, "User does not exist")
        
        return redirect("/")

    # If request is not POST, render login form (assuming you have a login form)
    return render(request, 'login.html')

def success(request):
    return render(request,'success.html')
