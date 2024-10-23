from django.urls import path
from . import views

urlpatterns =[
    path("personaldetails/",views.p_details,name='personaldetails_view'),
    path("plan/",views.joinus_plan,name='joinus_plan_view'),
    path("setpassword/",views.setpassword,name='setpassword_view'),
    path("reg/",views.reg,name='reg_view')
]
