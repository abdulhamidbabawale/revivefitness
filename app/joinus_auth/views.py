from django.shortcuts import render,redirect
from ..site_data.models import User,Classes,Plans
from django.http import JsonResponse
import requests

# Create your views here.
  
def p_details(request):
     context={
          'active_page':'p_details',
     }
     return render(request,'joinus_personaldetails.html',context)
def joinus_plan(request):
     classes=Classes.objects.all().values()
     platinum_plan=Plans.objects.filter(plan_name='platinum').values().first()
     standard_plan=Plans.objects.filter(plan_name='standard').values().first()
    #  selected_plan=request.COOKIES.get('selectedplan', '1')

    #get selected plan id from cookiews if cookies is empty default if 2(platinum)
     selected_id=request.COOKIES.get('selectedplan') or 2


     #use the selected plan id to get the plan name
     selected_plan=Plans.objects.filter(id=selected_id).values_list('plan_name', flat=True).first()

     #get plan cost for platinum and standard
     standard_cost = Plans.objects.filter(plan_name='standard').values_list('plan_price', flat=True).first()
     platinum_cost = Plans.objects.filter(plan_name='platinum').values_list('plan_price', flat=True).first()

     #multiply plan cost based on duration and use '{:,}' to add ' , ' symbol to the price
     platinum_monthly='{:,}'.format(platinum_cost)
     joinus_plan.platinum_quterly= '{:,}'.format(int(platinum_cost * 2.4))
     platinum_yearly='{:,}'.format(int(platinum_cost * 7.4))
     standard_monthly='{:,}'.format(standard_cost)
     joinus_plan.standard_quterly= '{:,}'.format(int(standard_cost * 2.4))
     standard_yearly='{:,}'.format(int(standard_cost * 7.4))
     duration_cost={
          'platinum_quterly':joinus_plan.platinum_quterly,
          'platinum_yearly':platinum_yearly,
          'platinum_monthly':platinum_monthly,
          'standard_monthly':standard_monthly,
          'standard_quterly':joinus_plan.standard_quterly,
          'standard_yearly': standard_yearly,
     }
     context={
          'classes':classes,
          'platinum_plan':platinum_plan,
          'standard_plan':standard_plan,
          'selected_plan':selected_plan,
          'duration_cost':duration_cost,
          'active_page':'joinus_plan',

     }
     return render(request,'joinus_plan.html',context)
# def join_cookies(request):
#     selected_plan=request.COOKIES.get('selectedplan', 'Not selected')
#     return JsonResponse({'selected_plan':selected_plan})


def setpassword(request):
     return render(request,'setpassword.html')

def reg(request):
     if request.method == 'POST':
          email= request.POST.get('email')
          password= request.POST.get('password')
          user = User.objects.create_user(email=email, password=password)
          user.save()

     return render(request,'register.html')

# def plan_data(request):
#      if request.method == 'POST':
#           userid=
#           planid
#           plan_duration
#           total_price


def registration_form(request):
     if request.method == 'POST':
          fname=request.POST.get('fname')
          lname=request.POST.get('lname')
          phone_number=request.POST.get('phone_number')

          gender=request.POST.get('gender')
          address=request.POST.get('address')
          city=request.POST.get('city')
          state=request.POST.get('state')
          zip_code=request.Post.get('zip_code')
          country=request.POST.get('country')
          plan_data=request.POST.get('plan_duration')
