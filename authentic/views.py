from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.
def login_page(request):
    if(request.method == 'POST'):
        username = request.POST.get('email')
        password = request.POST.get('password')

        if not (User.objects.filter(username = username).exists()):
            messages.error(request, "Username Not found")
            return redirect('/')    
        user = authenticate(username=username , password = password)

        if not (user==None):
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, "Invalid password")
            return redirect('/')
    return render(request ,'authentic/login.html')


    
def register(request):
    if(request.method=='POST'):
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('email')

        if(User.objects.filter(username = username).exists()):
            messages.error(request, 'User already exists. Please use a different email or try logging in')
            return redirect('/register/')
        
        user = User.objects.create(
            username = username,
            first_name = firstName,
            last_name = lastName
        )
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully. Try logging in.')
        return redirect('/')
    return render(request, 'authentic/register.html')