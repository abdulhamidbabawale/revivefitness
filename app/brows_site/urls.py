from django.urls import path
from . import views

urlpatterns =[
    path("home/",views.home,name='home_view'),
    path("classes/",views.classes,name='classes_view'),
]
