from django.shortcuts import render,redirect
from time import localtime, strftime
import random
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request,'index.html')

def process_money(request):
    location = request.POST.get('location')
    if location == 'farm' or location == 'house' or location == 'cave':
        request.session['x']=random.randint(10,20)
        request.session['counter'] +=  request.session['x']
        message = f"you entered a {location} and earned { request.session['x']}" 
    else:
        request.session['rdm'] = random.randint(-50,50) 
        request.session['counter'] += request.session['rdm']
        if  request.session['rdm'] > 0:
            message = f"you completed a quest and earned {request.session['rdm']}"
        else:
            message = f"you failed a quest and lost {request.session['rdm']}, OUCH!"
    request.session['activities'].append({
    'timestamp': strftime("%Y-%m-%d %H:%M:%S", localtime()),  # Add current local time
    'message': message })  
    return redirect('/')  
