from django.shortcuts import render,redirect
from .models import *

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors':authors,
    }
    return render(request,'index.html',context)
def show_authors(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors':authors,
    }
    return render(request,'add_autho
                  r.html',context)

def book_add(request):
    if request.method == "POST":
        title_from_form = request.POST.get('title')
        description_from_form = request.POST.get('description')
        Book.objects.create(title = title_from_form, description = description_from_form)
        return redirect('/')
    return render(request,"index.html")

def views_books(request,id):
    book = Book.objects.get(id = id)
    authors = Author.objects.all()
    context = {
        'book': book,
        'authors' : authors,
    }
    return render(request,"view_books.html",context)

def add_authors(request):
    if request.method == "POST":
        first_name_from_form = request.POST.get('first_name')
        last_name_from_form = request.POST.get('last_name')
        notes_from_form = request.POST.get('notes')
        Author.objects.create(first_name = first_name_from_form, last_name = last_name_from_form, notes = notes_from_form)
        return redirect('/')
    return render(request,'add_author.html')
    
def show_author(request,id):
    author = Author.objects.get(id=id)
    books = Book.objects.all()
    context = {
        'author':author,
        'books':books,
    }
    return render(request,"view_author.html",context)

def add_book_to_author(request):
    if request.method == "POST":
        book_id_from_form = request.POST.get('book')
        author_id_from_form = request.POST.get('author_id')
        book = Book.objects.get(id = book_id_from_form)
        author = Author.objects.get(id = author_id_from_form)
        author.books.add(book)
        return redirect(f"/authors/{author_id_from_form}")
    return render(request,'view_author.html')