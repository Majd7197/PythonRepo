from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    return render(request, 'index.html')

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)

def add_show(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            title_from_form = request.POST.get('title')
            network_from_form = request.POST.get('network')
            release_date_from_form = request.POST.get('release_date')
            description_from_form = request.POST.get('description')
            new_show = Show.objects.create(
                title=title_from_form, 
                network=network_from_form, 
                release_date=release_date_from_form, 
                description=description_from_form
            )
            return redirect(f'/shows/{new_show.id}/')

def show_info(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'show_info.html', context)

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

def edit_show_page(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, "edit_show.html", context)

def edit_show(request):
    if request.method == "POST":
        show_id_from_form = request.POST.get('id_show')
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id_from_form}/edit')
        else:
            show = Show.objects.get(id=show_id_from_form)
            show.title = request.POST.get('title')
            show.network = request.POST.get('network')
            show.release_date = request.POST.get('release_date')
            show.description = request.POST.get('description')
            show.save()
            return redirect(f'/shows/{show_id_from_form}/')
