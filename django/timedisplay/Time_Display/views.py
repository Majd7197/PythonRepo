from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime('%B %d, %Y %I:%M %p', gmtime())
    }
    return render(request,'index.html', context)

def time(request):
    return redirect('/')




    


