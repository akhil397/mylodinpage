import email
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



#user agil pass agil123
# Create your views here.


def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        auth_user=(request,user)
        return redirect('/')

    return render (request,'registration/login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
            
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name,last_name=last_name,email=email, password=password)
                user.save()
    				
                return redirect('/')
                    
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'registration/register.html',{'messages':messages})

def chagepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/changepass.html', {
        'form': form
    })
    
