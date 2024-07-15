from django.shortcuts import render,HttpResponse,redirect
from books_authors_with_templates_app.models import Book,Author

def index(request):
    context = {
        'books' : Book.objects.all(),
        'authors' : Author.objects.all()
    }
    return render(request,'index.html',context)

def add_book(request):
    if request.method == "POST":
        title_from_form = request.POST.get('title')
        description_from_form = request.POST.get('description')
        Book.objects.create(title = title_from_form, desc = description_from_form)
    return redirect('/')
# Create your views here.
