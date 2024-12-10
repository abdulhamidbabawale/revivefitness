from django.shortcuts import render,redirect
from ..site_data.models import User,Classes,Plans
from django.http import JsonResponse
import requests
from .resources import Resource
from django.conf import settings
# Create your views here.  heg5yingf6mh44s

res=Resource()
res.plan_duration_cost()
# res.cookies_data(request)
def payment(request):
     e=request.session.get('email')
     total_price=res.plan_price(request)
    #  print(total_price)
     payment_info=res.payment1(request,total_price,e)
     return payment_info



def verify_payment(request):
    #  reference= "rr57di4o6l"
     reference=request.session.get('reference')
     verify=res.verify_payment1(reference)
     return verify


def p_details(request):
     if request.method=="POST":

          fname=request.POST.get('fname')
          lname=request.POST.get('lname')
          phone_number=request.POST.get('phone_number')
          email=request.POST.get('email')

          gender=request.POST.get('gender')
          address=request.POST.get('address')
          city=request.POST.get('city')
          state=request.POST.get('state')
          # zip_code=request.Post.get('zip_code')
          # country=request.POST.get('country')
          # plan_data=request.POST.get('plan_duration')
          request.session['fname'] = fname
          request.session['lname'] = lname
          request.session['email'] = email
          request.session['phone_number'] = phone_number
          request.session['gender'] = gender
          request.session['address'] = address
          request.session['city'] = city
          request.session['state'] = state
          # request.session['plan_data'] = plan_data
          res.cookies_data(request)
          request.session['selectedplan_id'] = Resource.cookies_data.selected_plan_id
          request.session['selectedclass_id'] = Resource.cookies_data.selected_Class_id
          request.session['selectedplan_duration_id'] = Resource.cookies_data.plan_Duration_id
          payment(request)
          payment_page=request.session.get('payment_page_url')
          return redirect (payment_page)
     res.cookies_data(request)
     print(Resource.cookies_data.selected_plan_id)
     print(request.session.get('fname', 'Key not found'))
     print(request.session.get('lname', 'Key not found'))
     print(request.session.get('email', 'Key not found'))
     print(request.session.get('gender', 'Key not found'))
     context={
          'active_page':'p_details',
          'payment_page':request.session.get('payment_page_url')
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
    #  platinum_monthly='{:,}'.format(platinum_cost)
    #  platinum_quterly= '{:,}'.format(int(platinum_cost * 2.4))
    #  platinum_yearly='{:,}'.format(int(platinum_cost * 7.4))
    #  standard_monthly='{:,}'.format(standard_cost)
    #  standard_quterly= '{:,}'.format(int(standard_cost * 2.4))
    #  standard_yearly='{:,}'.format(int(standard_cost * 7.4))
     duration_cost={
          'platinum_quterly': Resource.plan_duration_cost.platinum_quterly,
          'platinum_yearly':Resource.plan_duration_cost.platinum_yearly,
          'platinum_monthly':Resource.plan_duration_cost.platinum_monthly,
          'standard_monthly':Resource.plan_duration_cost.standard_monthly,
          'standard_quterly':Resource.plan_duration_cost.standard_quterly,
          'standard_yearly': Resource.plan_duration_cost.standard_yearly,
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

def success_page(request):
     context={
        'active_page':'success_page',
     }
     return render(request,'success.html',context)
# def registration_form(request):
#      if request.method == 'POST':
#           fname=request.POST.get('fname')
#           lname=request.POST.get('lname')
#           phone_number=request.POST.get('phone_number')

#           gender=request.POST.get('gender')
#           address=request.POST.get('address')
#           city=request.POST.get('city')
#           state=request.POST.get('state')
#           zip_code=request.Post.get('zip_code')
#           country=request.POST.get('country')
#           plan_data=request.POST.get('plan_duration')
