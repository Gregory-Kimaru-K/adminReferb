from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import CustomUser
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and isinstance(user, CustomUser):
            login(request, user)
            return JsonResponse({'success' : 'True', 'redirect_url' : '/home/'})
        
        else:
            return JsonResponse({'success' : 'False', 'message' : 'Invalid credentials'})


    return render(request, 'registration/login.html')

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='/login')
def admin_view(request):
    context = {
        'username' : request.user.username
    }
    return render(request, 'body_temp/main.html', context)

def adminstration(request):
    return render(request, 'body_temp/auth_temp/main.html')

def user_table(request):
    return render(request, 'body_temp/auth_temp/usertab.html')

def grp_table(request):
    return render(request, 'body_temp/auth_temp/grptab.html')

def message_table(request):
    return render(request, 'body_temp/msgtab.html')
