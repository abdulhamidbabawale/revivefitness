from django.shortcuts import render,redirect
from app.site_data.models import User
from django.contrib.auth import login as lt,authenticate
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(request, email=email, password=password)
        except:
             messages.error(request, f"User {email} Not Found....")
             return redirect("home_view")
        if user is not None:
            lt(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect("home_view")

        else:
            messages.error(request, "Username or Password does not match...")
    return render(request,'login.html')
