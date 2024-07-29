from django.shortcuts import render

# Create your views here.
def admin_view(request):
    return render(request, 'base.html')

def login_view(request):
    return render(request, 'registration/login.html')