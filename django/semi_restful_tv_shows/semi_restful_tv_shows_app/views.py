from django.shortcuts import render,redirect
from .models import Show
def index(request):
    return render(request,'index.html')

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows' : shows
    }
    return render(request,'shows.html',context)

def add_show(request):
    if request.method == "POST":
        title_from_form = request.POST.get('title')
        network_from_form = request.POST.get('network')
        release_date_from_form = request.POST.get('release_date')
        description_from_form = request.POST.get('description')
        new_show = Show.objects.create(title = title_from_form, network = network_from_form, release_date = release_date_from_form, description = description_from_form)
        new_show_id = new_show.id
        return redirect(f'/shows/{new_show_id}/')
        
def show_info(request,id):
    show = Show.objects.get(id=id)
    context = {
        'show':show
    }
    return render(request,'show_info.html',context)
def delete_show(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')
def edit_show_page(request,id):
    show = Show.objects.get(id=id)
    context = {
        'show' : show
    }
    
    return render(request,"edit_show.html",context)

def edit_show(request):
    show_id_from_form = request.POST.get('id_show')
    show = Show.objects.get(id=show_id_from_form)
    updated_title_from_form = request.POST.get('title')
    updated_network_from_form = request.POST.get('network')
    updated_release_date_from_form = request.POST.get('release_date')
    updated_description_from_form = request.POST.get('description') 
    show.title = updated_title_from_form
    show.network = updated_network_from_form
    show.release_date = updated_release_date_from_form
    show.description = updated_description_from_form
    show.save()
    return redirect(f'/shows/{show_id_from_form}/')