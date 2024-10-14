from django.shortcuts import render

# Create your views here.
def p_details(request):
     return render(request,'joinus_personaldetails.html')
def joinus_plan(request):
     return render(request,'joinus_plan.html')
