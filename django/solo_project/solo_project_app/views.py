from django.shortcuts import render, redirect
from .models import User, Role, Subscription,Class
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
        photo = request.FILES.get('photo')
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
            password=password,
            photo = photo,
        )
        request.session['first_name'] = first_name

        # Handle role
        role_title = request.POST.get('role')
        custom_role = request.POST.get('custom_role')
        custom_description = request.POST.get('custom_description')

        if role_title == 'custom' and custom_role:
            role = Role.objects.create(
                title=custom_role,
                description=custom_description,
                user=user
                
            )
        elif role_title == 'member':
            role = Role.objects.create(
                title=role_title,
                description='this is a member',
                user=user
            )
        elif role_title == 'trainer':
            role = Role.objects.create(
                title=role_title,
                description='this is a trainer',
                user=user
            )
<<<<<<< HEAD
=======

>>>>>>> a491f750c55dc73f21525cc08d514e82abec15ab
        return redirect('/users')

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
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        
    }
    return render(request,'subscriptions.html',context)

def add_subscription(request, id):
    start_date =  date.today()
    end_date = start_date + timedelta (days = 30)
    Subscription.objects.create(start_date = start_date , end_date = end_date, user = User.objects.get(id = id))
    return redirect('/subscriptions')

def classes(request):
    def index(request):
    # if request.method == "POST":
        # errors = User.objects.basic_validator(request.POST)
        # if errors:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect('/')

        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # date_of_birth = request.POST.get('dateofbirth')
        # phone_number = request.POST.get('phone_number')
        # email = request.POST.get('email')
        # password = generate_random_password()
        # # password = request.POST.get('password')
        # # confirm_password = request.POST.get('confirm_password')


        # # # Check if passwords match
        # # if password != confirm_password:
        # #     messages.error(request, "Passwords do not match.")
        # #     return redirect('/')

        # # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # # Create User
        # user = User.objects.create(
        #     first_name=first_name,
        #     last_name=last_name,
        #     dateofbirth=date_of_birth,
        #     phone_number=phone_number,
        #     email=email,
        #     password=password
        # )
        # request.session['first_name'] = first_name

        # # Handle role
        # role_title = request.POST.get('role')
        # custom_role = request.POST.get('custom_role')
        # custom_description = request.POST.get('custom_description')

        # if role_title == 'custom' and custom_role:
        #     role = Role.objects.create(
        #         title=custom_role,
        #         description=custom_description,
        #         user=user
                
        #     )
        # elif role_title == 'member':
        #     role = Role.objects.create(
        #         title=role_title,
        #         description='this is a member',
        #         user=user
        #     )
        # elif role_title == 'trainer':
        #     role = Role.objects.create(
        #         title=role_title,
        #         description='this is a trainer',
        #         user=user
        #     )
        return redirect('/users')

    content = {
        'roles': Role.objects.all(),
        'users': User.objects.all(),
        'classes':Class.objects.all(),
    }
    return render(request, 'classes.html', content)
    
def add_class(request):
    title_from_form = request.POST.get('title')
    description_from_form = request.POST.get('description')
    max_size_from_form = request.POST.get('max_size')
    user_id_from_form = request.POST.get('trainer')
    class_id_from_form = request.POST.get('class_id')
    
    # Create the class object
    a_class = Class.objects.create(
        title=title_from_form,
        description=description_from_form,
        max_size=max_size_from_form
    )
    
    # Get the user object and add the class to that user
    user = User.objects.get(id=user_id_from_form)
    user.classes.add(a_class)
    
    return redirect('/classes')
        
