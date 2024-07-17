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
        