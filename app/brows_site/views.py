from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'index.html',{'active_page':'home'})


def classes(request):
     return render(request,'classes.html',{'active_page':'classes'})

def aboutus(request):
     return render(request,'aboutus.html',{'active_page':'aboutus'})

def membership(request):
     return render(request,'membership.html',{'active_page':'membership'})
