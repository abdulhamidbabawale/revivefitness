from django.urls import path
from . import views

urlpatterns =[
    path("home/",views.home,name='home_view'),
    path("classes/",views.classes,name='classes_view'),
    path("aboutus/",views.aboutus,name='aboutus_view'),
    path("membership/",views.membership,name='membership_view'),
    path("",views.default_view)
]
