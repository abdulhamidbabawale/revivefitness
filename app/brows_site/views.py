from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from app.site_data.models import User,Classes

# Create your views here.
def home(request):

    return render(request,'index.html',{'active_page':'home'})


def classes(request):
     all_class=Classes.objects.all().values()
     context={
'active_page':'classes',
'all_class':all_class,
     }

     return render(request,'classes.html',context)

def aboutus(request):
     return render(request,'aboutus.html',{'active_page':'aboutus'})

def membership(request):
     return render(request,'membership.html',{'active_page':'membership'})

def default_view(request):
    return redirect(home)
