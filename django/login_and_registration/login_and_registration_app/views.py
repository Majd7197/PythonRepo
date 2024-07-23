from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        print("THIS IS A POST REQUEST !!!!!!!!!!")
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            first_name_from_form = request.POST.get('first_name')
            last_name_from_form = request.POST.get('last_name')
            email_from_form = request.POST.get('email')
            password = request.POST.get('password')
            birthday = request.POST.get('birthday')
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)        
            User.objects.create(first_name=first_name_from_form ,last_name = last_name_from_form, email = email_from_form, password = pw_hash,birthday=birthday)
            request.session['first_name'] = request.POST.get('first_name')
            return redirect('/success')
    print("THIS IS A GET REQUEST !!!!!!")
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
            messages.error(request, "Incorrect Username or password")
        else:
            # Handle the case where no users were found
            messages.error(request, "User does not exist")
        
        return redirect("/")

    # If request is not POST, render login form (assuming you have a login form)
    return render(request, 'login.html')

def success(request):
    if 'first_name' not in request.session:
        print("USER IS NOT IN THE SESSION")
        return redirect('/')
    return render(request, 'success.html')

def logout(request):
    request.session.flush()
    return redirect('/')
