from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")
def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")
def destroy(request,number):
    return redirect("/blogs")
def blogs_json(request):
    blogs_data = [
        {'title': 'Blog Title 1', 'content': 'Blog Content 1'},
        {'title': 'Blog Title 2', 'content': 'Blog Content 2'},
    ]
    return JsonResponse({'blogs': blogs_data})

