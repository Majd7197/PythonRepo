from django.shortcuts import render,HttpResponse,redirect
def index(request):
    if 'key_name' in request.session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")
    if 'counter' not in request.session:
        request.session['counter'] = 0

    request.session['counter'] += 1

    return render(request, "main_page.html")

def destroy_session(request):
    # Clear the session data
    request.session.flush()
    # Optionally, redirect to another page
    return redirect('/')
def counter_two(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 2
    return render(request,"main_page.html")
def counter_by_any(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    try:
        request.session['counter'] += int(request.POST['quantity'])
    except ValueError:
        request.session['counter'] += 0  

    return render(request,"main_page.html")