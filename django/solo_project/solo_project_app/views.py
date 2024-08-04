from django.shortcuts import render, redirect
from .models import User, Role, Subscription
from django.contrib import messages
from datetime import date, timedelta
import bcrypt
import secrets
import string
from time import gmtime, strftime

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def index(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('dateofbirth')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = generate_random_password()
        # password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password')


        # # Check if passwords match
        # if password != confirm_password:
        #     messages.error(request, "Passwords do not match.")
        #     return redirect('/')

        # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # Create User
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            dateofbirth=date_of_birth,
            phone_number=phone_number,
            email=email,
            password=password
        )
        request.session['first_name'] = first_name

        # Handle role
        role_title = request.POST.get('role')
        custom_role = request.POST.get('custom_role')
        custom_description = request.POST.get('custom_description')

        if role_title == 'custom' and custom_role:
            role, created = Role.objects.get_or_create(
                title=custom_role,
                defaults={
                    'description': custom_description,
                    'user': user  # Associate role with the created user
                }
            )
        elif role_title == 'member':
            # Assuming you want to handle predefined roles here
            role, created = Role.objects.get_or_create(
                title=role_title,
                defaults={
                    'description': 'this is a member',
                    'user': user  # Associate role with the created user
                }
            )
        elif role_title == 'trainer':
            role, created = Role.objects.get_or_create(
                title=role_title,
                defaults={
                    'description': 'this is a trainer',
                    'user': user  # Associate role with the created user
                }
            )

        return redirect('/')

    content = {
        'roles': Role.objects.all(),
        'users': User.objects.all()
    }
    return render(request, 'index.html', content)

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                request.session['userid'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                return redirect('/dashboard')
            messages.error(request, "Incorrect password.")
        else:
            messages.error(request, "User does not exist.")
        return redirect("/")
    return render(request, 'login.html')

def subscriptions(request):
    ## mesh jahizzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    context = {
        'users' : User.objects.all(),
        'roles': Role.objects.all(),
        'subscriptions' : Subscription.objects.all(),
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'subscriptions.html',context)

def add_subscription(request, id):
    start_date =  date.today()
    end_date = start_date + timedelta (days = 30)
    Subscription.objects.create(start_date = start_date , end_date = end_date, user = User.objects.get(id = id))
    return redirect('/subscriptions')

from django.shortcuts import render
from time import gmtime, strftime
    


        
