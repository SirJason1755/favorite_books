from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):    
    
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for k , v in errors.items():
            messages.error(request, v)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw
    )

    messages.info(request,'sucess; please log in')    

    return redirect('/')


def login(request):

    try:
        users = User.objects.get(email = request.POST['email'])
    except:
        messages.error(request, 'No user with this email exists.')
        return redirect('/')


    if not bcrypt.checkpw(request.POST['password'].encode(),users.password.encode()):
        messages.error(request,'Password is incorrect.')
        return redirect('/')

    request.session['user_id'] = users.id
    request.session['user_email'] = users.email
    return redirect('/favorite')



def destroy(request):
    request.session.clear()
    return redirect('/')


