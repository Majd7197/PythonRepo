from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    return render(request, "index.html")

def number_guess(request):
    if request.method == 'POST':
        if 'counter' not in request.session:
            request.session['counter'] = 1
        else:
            request.session['counter'] += 1
        
        guessed_number = int(request.POST['quantity'])  
        number_random = request.session['number'] 
        
        if guessed_number < number_random:
            request.session['message'] = 'Too low!'
        elif guessed_number > number_random:
            request.session['message'] = 'Too high!'
        else:
            request.session['message'] = 'You guessed it!'
            request.session.pop('number')  # Remove the number so a new game can start
    
    return redirect('index')



def reset(request):
    if 'number' in request.session:
        request.session.pop('number',None)
        request.session.flush()
    return redirect('/')