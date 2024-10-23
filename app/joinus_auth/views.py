from django.shortcuts import render,redirect
from ..site_data.models import User

# Create your views here.
def p_details(request):
     return render(request,'joinus_personaldetails.html')
def joinus_plan(request):
     return render(request,'joinus_plan.html')
def setpassword(request):
     return render(request,'setpassword.html')
def reg(request):
     if request.method == 'POST':
          email= request.POST.get('email')
          password= request.POST.get('password')
          user = User.objects.create_user(email=email, password=password)
          user.save()

     return render(request,'register.html')
