from django.shortcuts import render,HttpResponse,redirect
from books_authors_with_templates_app.models import Book,Author

def index(request):
    context = {
        'books' : Book.objects.all(),
        'authors' : Author.objects.all()
    }
    return render(request,'index.html',context)

def display_authors(request):
    context = {
        'books' : Book.objects.all(),
        'authors' : Author.objects.all()
    }
    return render(request,'display_authors.html',context)

def add_book(request):
    if request.method == "POST":
        title_from_form = request.POST.get('title')
        description_from_form = request.POST.get('description')
        Book.objects.create(title = title_from_form, desc = description_from_form)
    return redirect('/')
def add_author(request):
    if request.method == "POST":
        first_name_from_form = request.POST.get('first_name')
        last_name_from_form = request.POST.get('last_name')
        notes_from_form = request.POST.get('notes')
        Author.objects.create(first_name = first_name_from_form, last_name = last_name_from_form, notes = notes_from_form)
    return redirect('/authors')

def get_book(request,id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    context = {
        'book' : book,
        'authors': authors
    }
    return render(request,'book_details.html',context)

def get_author(request,id):
    author = Author.objects.get(id=id)
    books = Book.objects.all()
    context = {
        'author' : author,
        'books' : books,
    }
    return render(request,'author_details.html',context)

def add_book_to_author(request):
    if request.method == "POST":
        book_id = request.POST.get('book')
        author_id = request.POST.get('author_id')
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=author_id)
        author.books.add(book)
        return redirect(f'/author/{author.id}/')
    return HttpResponse("Invalid request or operation")
    
def add_author_to_book(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        author_id = request.POST.get('author')
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
        return redirect(f'/books/{book.id}/')
    return HttpResponse("Invalid request or operation")