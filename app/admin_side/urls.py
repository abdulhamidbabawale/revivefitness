from django.urls import path,include
from . import views

urlpatterns=[
    path('classes/',views.admin_classes,name='admin_classes_view'),
]

