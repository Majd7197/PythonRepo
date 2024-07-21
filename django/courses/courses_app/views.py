from django.shortcuts import render,redirect
from .models import Course
from django.contrib import messages

def index(request):
    
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            context = {
                'courses': Course.objects.all() 
            }
            return render(request,'index.html',context)
        else:
            name_from_form = request.POST.get('name')
            description_from_form = request.POST.get('description')
            Course.objects.create(name=name_from_form,description = description_from_form)
            return redirect('/')
    context = {
    'courses': Course.objects.all()  # Ensure context is updated
    }
    return render(request, 'index.html', context)

def delete_course_page(request,id):
    context = {
        'course' : Course.objects.get(id=id),
    }
    return render(request,'delete_course.html',context)
    
def do_not_delete_course(request):
    return redirect('/')
def delete_course(request):
    course_id = request.POST.get('course_id')
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')