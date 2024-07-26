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
            email_from_form = request.POST.get('email')
            password = request.POST.get('password')
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)        
            User.objects.create(first_name=first_name_from_form ,last_name = last_name_from_form, email = email_from_form, password = pw_hash)
            request.session['first_name'] = request.POST.get('first_name')
            return redirect('/dashboard')
    return render(request, 'index.html')

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

def success(request):
    if 'first_name' not in request.session:
        print("USER IS NOT IN THE SESSION")
        return redirect('/')
    user_id = request.session.get('userid')
    pies = Pie.objects.filter(user_id = user_id )
    context = {
        'pies': pies
    }    
    return render(request, 'success.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

def add_pie(request):
    if request.method == "POST":
        errors = Pie.objects.basic_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard')
        else:
            name_from_form = request.POST.get('name')
            filling_from_form = request.POST.get('filling')
            crust_from_form = request.POST.get('crust') 
            id_from_form = request.POST.get('user_id')     
            Pie.objects.create(name = name_from_form ,filling = filling_from_form , crust = crust_from_form, user = User.objects.get(id =id_from_form ))
            return redirect('/dashboard')
    return render(request, 'success.html')

def edit_pie(request,id):
    if 'first_name' not in request.session:
        return redirect('/')
    pie = Pie.objects.get(id = id)
    context = {
        'pie': pie
    }
    return render(request,"edit_pie.html",context)

def update_pie(request):
    if request.method == "POST":
        pie_id_from_form = request.POST.get('pie_id')
        errors = Pie.objects.basic_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/pies/edit/{pie_id_from_form}")
        else:
            name_from_form = request.POST.get('name')
            filling_from_form = request.POST.get('filling')
            crust_from_form = request.POST.get('crust')  
            pie = Pie.objects.get(id = pie_id_from_form)
            pie.name = name_from_form
            pie.filling = filling_from_form
            pie.crust = crust_from_form
            pie.save()
            return redirect('/dashboard')
    return render(request, 'success.html')

def delete_pie(request,id):
    if 'first_name' not in request.session:
        print("USER IS NOT IN THE SESSION")
        return redirect('/')
    pie = Pie.objects.get(id = id)
    pie.delete()
    return redirect('/dashboard')

def show_all_pies(request):
    if 'first_name' not in request.session:
        return redirect('/')
    pies = Pie.objects.all()
    users = User.objects.all()
    context = {
        'pies':pies,
        'users' : users,
    }
    return render(request,"all_pies.html",context)
    
def view_pie(request,id):
    if 'first_name' not in request.session:
        return redirect('/')
    pie = Pie.objects.get(id = id)
    context= {
        'pie':pie,
        
    }
    
    return render(request,"view_pie.html",context)